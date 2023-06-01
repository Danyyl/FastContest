from datetime import datetime
from typing import List

from sqlalchemy import select, insert, update
from sqlalchemy.orm import selectinload
from tasks.models import Topic, Task, Tag, TaskTag, UserTask
from tasks.schemas import TopicScheme, TopicCreate, TopicUpdate, TaskScheme, TaskCreate, TaskUpdate, TagScheme, \
    TagCreate, TaskTagScheme, TaskTagCreate, UserTaskScheme, UserTaskCreate, UserTaskUpdate

from tasks.utils import StatusEnum


class BaseManager:

    @staticmethod
    async def create_stmt(stmt, session):
        try:
            await session.execute(stmt)
            await session.commit()
        except Exception as e:  # ToDo Modify
            return {
                "status": 500,
                "data": f"Error - {e}"
            }
        return {
            "status": 200,
            "data": "created"
        }

    @staticmethod
    async def update_stmt(stmt, session):
        try:
            await session.execute(stmt)
            await session.commit()
        except Exception as e:  # ToDo Modify
            return {
                "status": 500,
                "data": f"Error - {e}"
            }
        return {
            "status": 200,
            "data": "updated"
        }

    @staticmethod
    async def get_many(session, query):
        result = await session.execute(query)
        data = [temp[0] for temp in result.all()]
        return data

    @staticmethod
    async def get_one_by_id(session, query):
        result = await session.execute(query)
        data = result.first()
        if data:
            return data[0]


class TaskManager:

    @staticmethod
    async def get_tasks(session) -> List[TaskScheme]:
        query = select(Task).options(selectinload(Task.topic), selectinload(Task.tags).subqueryload(TaskTag.tag))
        return await BaseManager.get_many(session, query)

    @staticmethod
    async def get_task(session, task_id) -> TaskScheme:
        query = select(Task).where(Task.id == task_id).options(selectinload(Task.topic))
        return await BaseManager.get_one_by_id(session, query)

    @staticmethod
    async def create_task(session, task_obj) -> dict:
        stmt = insert(Task).values(**task_obj.dict())
        return await BaseManager.create_stmt(stmt, session)

    @staticmethod
    async def add_tag_to_task(session, tag_id, task_id) -> dict:
        stmt = insert(TaskTag).values(tag_id=tag_id, task_id=task_id)
        return await BaseManager.create_stmt(stmt, session)

    @staticmethod
    async def get_tasks_by_tag(session, tag_id) -> List[TaskScheme]:
        query = select(Task).join(Task.tags).\
            where(TaskTag.tag_id == tag_id).options(selectinload(Task.topic), selectinload(Task.tags))
        return await BaseManager.get_many(session, query)


class TopicManager:

    @staticmethod
    async def get_topics(session) -> List[TopicScheme]:
        query = select(Topic)
        return await BaseManager.get_many(session, query)

    @staticmethod
    async def get_topic(session, topic_id) -> TopicScheme:
        query = select(Topic).where(Topic.id == topic_id)
        return await BaseManager.get_one_by_id(session, query)

    @staticmethod
    async def create_topic(session, topic_obj) -> dict:
        stmt = insert(Topic).values(**topic_obj.dict())
        return await BaseManager.create_stmt(stmt, session)


class TagManager:

    @staticmethod
    async def get_tags(session) -> List[TagScheme]:
        query = select(Tag)
        return await BaseManager.get_many(session, query)

    @staticmethod
    async def get_tag(session, tag_id) -> TagScheme:
        query = select(Tag).where(Tag.id == tag_id)
        return await BaseManager.get_one_by_id(session, query)

    @staticmethod
    async def create_tag(session, tag_obj) -> dict:
        stmt = insert(Tag).values(**tag_obj.dict())
        return await BaseManager.create_stmt(stmt, session)


class UserTaskManager:

    @staticmethod
    async def get_tasks(session, user_id) -> List[UserTaskScheme]:
        query = select(UserTask).where(UserTask.user_id == user_id).options(selectinload(UserTask.task))
        return await BaseManager.get_many(session, query)

    @staticmethod
    async def get_task(session, task_id, user_id) -> UserTaskScheme:
        query = select(UserTask).where(UserTask.user_id == user_id, UserTask.task_id == task_id).\
            options(selectinload(UserTask.task))
        return await BaseManager.get_one_by_id(session, query)

    @staticmethod
    async def create_task(session, task_id, user_id) -> dict:
        stmt = insert(UserTask).values(task_id=task_id, user_id=user_id)
        return await BaseManager.create_stmt(stmt, session)

    @staticmethod
    async def add_answer(session, task_id, user_id, answer) -> dict:
        stmt = update(UserTask).\
            where(UserTask.task_id == task_id, UserTask.user_id == user_id).\
            values(answer=answer, submitted=True, submitted_at=datetime.utcnow(), status=StatusEnum.draft.value)
        return await BaseManager.update_stmt(stmt, session)
