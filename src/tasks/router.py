from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from tasks.schemas import TopicScheme, TopicCreate, TopicUpdate, TaskScheme, TaskCreate, TaskUpdate, TagScheme, \
    TagCreate, TaskTagScheme, TaskTagCreate, UserTaskScheme, UserTaskCreate, Solution, UserTaskAnswer
from tasks.manager import TaskManager, TopicManager, TagManager, UserTaskManager
from database import get_async_session

from auth.router import current_active_user

router = APIRouter(
    prefix="",
    tags=[],
)


def default_params(session: AsyncSession = Depends(get_async_session), user: User = Depends(current_active_user)):
    return {
        "session": session,
        "user": user
    }


# Tasks
@router.get("", response_model=Optional[List[TaskScheme]], tags=["Tasks"])
async def get_tasks(common: dict = Depends(default_params)) -> Optional[List[TaskScheme]]:
    result = await TaskManager.get_tasks(common.get("session"))
    return result


@router.get("/{task_id}", response_model=Optional[TaskScheme], tags=["Tasks"])
async def get_task(task_id: int, common: dict = Depends(default_params)) -> Optional[TaskScheme]:
    result = await TaskManager.get_task(common.get("session"), task_id)
    return result


@router.get("/{task_id}/add_tag/", tags=["Tasks"])
async def add_tag_to_task(task_id: int, tag_id: int, common: dict = Depends(default_params)) -> dict:
    return await TaskManager.add_tag_to_task(common.get("session"), tag_id, task_id)


@router.get("/by_tag/", response_model=Optional[List[TaskScheme]], tags=["Tasks"])
async def get_tasks_by_tag(tag_id: int, common: dict = Depends(default_params)) -> Optional[List[TaskScheme]]:
    result = await TaskManager.get_tasks_by_tag(common.get("session"), tag_id)
    return result


@router.post("", tags=["Tasks"])
async def create_task(task: TaskCreate, common: dict = Depends(default_params)) -> dict:
    return await TaskManager.create_task(session=common.get("session"), task_obj=task)


# Topic
@router.get("/topic/", response_model=Optional[List[TopicScheme]], tags=["Topic"])
async def get_topics(common: dict = Depends(default_params)) -> Optional[List[TopicScheme]]:
    result = await TopicManager.get_topics(common.get("session"))
    return result


@router.get("/topic/{topic_id}", response_model=Optional[TopicScheme], tags=["Topic"])
async def get_topic(topic_id: int, common: dict = Depends(default_params)) -> Optional[TopicScheme]:
    return await TopicManager.get_topic(common.get("session"), topic_id)


@router.post("/topic", tags=["Topic"])
async def create_topic(topic: TopicCreate, common: dict = Depends(default_params)) -> dict:
    return await TopicManager.create_topic(session=common.get("session"), topic_obj=topic)


# Tag
@router.get("/tag/", response_model=Optional[List[TagScheme]], tags=["Tag"])
async def get_tags(common: dict = Depends(default_params)) -> Optional[List[TagScheme]]:
    result = await TagManager.get_tags(common.get("session"))
    return result


@router.get("/tag/{tag_id}", response_model=Optional[TagScheme], tags=["Tag"])
async def get_tag(tag_id: int, common: dict = Depends(default_params)) -> Optional[TagScheme]:
    return await TagManager.get_tag(common.get("session"), tag_id)


@router.post("/tag", tags=["Tag"])
async def create_tag(tag: TagCreate, common: dict = Depends(default_params)) -> dict:
    return await TagManager.create_tag(session=common.get("session"), tag_obj=tag)


# User task
@router.get("/user_task/", response_model=Optional[List[UserTaskScheme]], tags=["Solutions"])
async def get_user_tasks(common: dict = Depends(default_params)) -> Optional[List[UserTaskScheme]]:
    result = await UserTaskManager.get_tasks(common.get("session"), common.get("user").id)
    return result


@router.get("/{task_id}/solutions", response_model=Optional[List[Solution]], tags=["Solutions"])
async def get_solutions_for_task(task_id: int,  common: dict = Depends(default_params)) -> Optional[List[Solution]]:
    user_task = await UserTaskManager.get_task(
        session=common.get("session"),
        task_id=task_id,
        user_id=common.get("user").id
    )
    if not user_task:
        return []
    return await UserTaskManager.get_solutions(common.get("session"), user_task.id)


# @router.get("/user_task/{task_id}", response_model=Optional[UserTaskScheme])
# async def get_user_task(task_id: int, common: dict = Depends(default_params)) -> Optional[UserTaskScheme]:
#     return await UserTaskManager.get_task(common.get("session"), task_id, common.get("user").id)


@router.post("/user_task", tags=["Solutions"])
async def create_user_task(task: UserTaskCreate, common: dict = Depends(default_params)) -> dict:
    return await UserTaskManager.create_task(
        session=common.get("session"),
        user_task=task,
        user_id=common.get("user").id
    )


@router.post("/user_task/add_answer/", tags=["Solutions"])
async def give_answer(data: UserTaskAnswer, common: dict = Depends(default_params)) -> dict:
    return await UserTaskManager.add_answer(
        session=common.get("session"),
        task_id=data.task_id,
        user_id=common.get("user").id,
        answer=data.answer
    )
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

