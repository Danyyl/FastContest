import asyncio

from fastapi import APIRouter, Depends

from auth.router import current_active_user
from auth.models import User
from fastapi_cache.decorator import cache

from test.tasks import some_long_task

router = APIRouter(
    prefix="",
    tags=[],
)


@router.get("/test_cache")
@cache(expire=60)
async def test_query_cache(user: User = Depends(current_active_user)):
    await asyncio.sleep(10)
    return "Ready"


@router.get("/test_celery_task")
async def test_celery_task(user: User = Depends(current_active_user)):
    some_long_task.delay()
    return "Ready"
