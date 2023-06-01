from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.models import User
from auth.schemas import ValidUser
from database import get_async_session

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)


@router.get("/test/{test_id}")
async def test(test_id: int, user: User = Depends(current_active_user)):
    return f"Hello - {user.name} your test id is {test_id}"


@router.get("")
async def get_users(session: AsyncSession = Depends(get_async_session)):
    query = select(User)
    result = await session.execute(query)
    data = [temp[0] for temp in result.all()]
    return {
        "status": 200,
        "data": data
    }


@router.post("")
async def add_users(user: ValidUser, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(User).values(**user.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "completed"}

