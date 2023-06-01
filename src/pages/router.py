import json

import requests
from typing import List, Optional

from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi_users import BaseUserManager, models
from fastapi_users.authentication import Strategy
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession


from database import get_async_session
from auth.auth import auth_backend
from auth.router import current_active_user
from auth.models import User
from pages.schemas import LoginForm
from auth.manager import get_user_manager
from starlette import status
from starlette.responses import Response, RedirectResponse

from tasks.schemas import UserTaskScheme, TaskScheme
from tasks.router import get_user_tasks, get_tasks

templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix="",
    tags=[],
)


def default_params(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return {
        "session": session,
        "user": user
    }


@router.get("")
async def index(
        request: Request,
        user: User = Depends(current_active_user),
        my_tasks: UserTaskScheme = Depends(get_user_tasks),
        tasks: TaskScheme = Depends(get_tasks),
):
    print(my_tasks)
    return templates.TemplateResponse(
        "pages/dashboard.html",
        {
            "request": request,
            "my_tasks": my_tasks,
            "tasks": tasks
        }
    )


# Login
@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        "accounts/auth-signin.html",
        {
            "request": request,
        }
    )


@router.post("/login")
async def authorized(request: Request, user_form: LoginForm = Depends(LoginForm.as_form),
                     user_manager: BaseUserManager[models.UP, models.ID] = Depends(get_user_manager),
                     strategy: Strategy[models.UP, models.ID] = Depends(auth_backend.get_strategy)):
    user = await user_manager.authenticate(user_form)
    response = await auth_backend.login(strategy, user)
    headers = response.headers
    response = RedirectResponse(url="/pages", status_code=status.HTTP_303_SEE_OTHER)
    response.headers.update(headers)
    return response


@router.get("/tasks")
def get_tasks(request: Request, user: User = Depends(current_active_user)):
    ...


@router.get("/temp")
def get_temp_page(request: Request, user: User = Depends(current_active_user)):
    return templates.TemplateResponse(
        "pages/test.html",
        {
            "request": request,
        }
    )

# @router.get("/{task_id}", response_model=Optional[TaskScheme])
# async def get_task(task_id: int, common: dict = Depends(default_params)) -> Optional[TaskScheme]:
#     return await TaskManager.get_task(common.get("session"), task_id)
#
#
# @router.get("/{task_id}/add_tag/")
# async def add_tag_to_task(task_id: int, tag_id: int, common: dict = Depends(default_params)) -> dict:
#     return await TaskManager.add_tag_to_task(common.get("session"), tag_id, task_id)
#
#
# @router.get("/by_tag/", response_model=Optional[List[TaskScheme]])
# async def get_tasks_by_tag(tag_id: int, common: dict = Depends(default_params)) -> Optional[List[TaskScheme]]:
#     result = await TaskManager.get_tasks_by_tag(common.get("session"), tag_id)
#     return result
#
#
# @router.post("")
# async def create_task(task: TaskCreate, common: dict = Depends(default_params)) -> dict:
#     return await TaskManager.create_task(session=common.get("session"), task_obj=task)
#
#
# # Topic
# @router.get("/topic/", response_model=Optional[List[TopicScheme]])
# async def get_topics(common: dict = Depends(default_params)) -> Optional[List[TopicScheme]]:
#     result = await TopicManager.get_topics(common.get("session"))
#     return result
#
#
# @router.get("/topic/{topic_id}", response_model=Optional[TopicScheme])
# async def get_topic(topic_id: int, common: dict = Depends(default_params)) -> Optional[TopicScheme]:
#     return await TopicManager.get_topic(common.get("session"), topic_id)
#
#
# @router.post("/topic")
# async def create_topic(topic: TopicCreate, common: dict = Depends(default_params)) -> dict:
#     return await TopicManager.create_topic(session=common.get("session"), topic_obj=topic)
#
#
# # Tag
# @router.get("/tag/", response_model=Optional[List[TagScheme]])
# async def get_tags(common: dict = Depends(default_params)) -> Optional[List[TagScheme]]:
#     result = await TagManager.get_tags(common.get("session"))
#     return result
#
#
# @router.get("/tag/{tag_id}", response_model=Optional[TagScheme])
# async def get_tag(tag_id: int, common: dict = Depends(default_params)) -> Optional[TagScheme]:
#     return await TagManager.get_tag(common.get("session"), tag_id)
#
#
# @router.post("/tag")
# async def create_tag(tag: TagCreate, common: dict = Depends(default_params)) -> dict:
#     return await TagManager.create_tag(session=common.get("session"), tag_obj=tag)
#
#
# # User task
# @router.get("/user_task/", response_model=Optional[List[UserTaskScheme]])
# async def get_user_tasks(common: dict = Depends(default_params)) -> Optional[List[UserTaskScheme]]:
#     result = await UserTaskManager.get_tasks(common.get("session"), common.get("user").id)
#     return result
#
#
# @router.get("/user_task/{task_id}", response_model=Optional[UserTaskScheme])
# async def get_user_task(task_id: int, common: dict = Depends(default_params)) -> Optional[UserTaskScheme]:
#     return await UserTaskManager.get_task(common.get("session"), task_id, common.get("user").id)
#
#
# @router.post("/user_task")
# async def create_user_task(task_id: int, common: dict = Depends(default_params)) -> dict:
#     return await UserTaskManager.create_task(
#         session=common.get("session"),
#         task_id=task_id,
#         user_id=common.get("user").id
#     )
#
#
# @router.post("/user_task/{task_id}/answer/")
# async def give_answer(task_id: int, answer: UserTaskUpdate, common: dict = Depends(default_params)) -> dict:
#     return await UserTaskManager.add_answer(
#         session=common.get("session"),
#         task_id=task_id,
#         user_id=common.get("user").id,
#         answer=answer.answer
#     )
# @router.get("/test/{test_id}")
# async def test(test_id: int, user: User = Depends(current_active_user)):
#     return f"Hello - {user.name} your test id is {test_id}"
#
#
# @router.get("")
# async def get_users(session: AsyncSession = Depends(get_async_session)):
#     query = select(User)
#     result = await session.execute(query)
#     data = [temp[0] for temp in result.all()]
#     return {
#         "status": 200,
#         "data": data
#     }
#
#
# @router.post("")
# async def add_users(user: ValidUser, session: AsyncSession = Depends(get_async_session)):
#     stmt = insert(User).values(**user.dict())
#     await session.execute(stmt)
#     await session.commit()
#     return {"status": "completed"}

