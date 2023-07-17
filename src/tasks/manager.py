from datetime import datetime
from typing import List, Optional
import aiohttp

from sqlalchemy import select, insert, update
from sqlalchemy.orm import selectinload
from tasks.models import Topic, Task, Tag, TaskTag, UserTask
from tasks.schemas import TopicScheme, TopicCreate, TopicUpdate, TaskScheme, TaskCreate, TaskUpdate, TagScheme, \
    TagCreate, TaskTagScheme, TaskTagCreate, UserTaskScheme, UserTaskCreate, Solution

from tasks.utils import StatusEnum


HOST = "http://host.docker.internal:8888/"
TOKEN = "Some_secret_key"


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
    def set_func_template(task):
        task.func_template = f"def {task.func_name}(inp):\n    pass"
        return task

    @staticmethod
    async def get_tasks(session) -> List[TaskScheme]:
        query = select(Task).options(selectinload(Task.topic), selectinload(Task.tags).subqueryload(TaskTag.tag))
        result = await BaseManager.get_many(session, query)
        return list(map(TaskManager.set_func_template, result))

    @staticmethod
    async def get_task(session, task_id) -> TaskScheme:
        query = select(Task).where(Task.id == task_id).options(selectinload(Task.topic),
                                                               selectinload(Task.tags).subqueryload(TaskTag.tag))
        result = await BaseManager.get_one_by_id(session, query)
        return TaskManager.set_func_template(result)

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
        query = select(Task).join(Task.tags). \
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
        query = select(UserTask).where(UserTask.user_id == user_id).options(selectinload(UserTask.task)).\
            order_by(UserTask.submitted_at.desc())
        return await BaseManager.get_many(session, query)

    @staticmethod
    async def get_task(session, task_id, user_id) -> UserTaskScheme:
        query = select(UserTask).where(UserTask.user_id == user_id, UserTask.task_id == task_id). \
            options(selectinload(UserTask.task))
        return await BaseManager.get_one_by_id(session, query)

    @staticmethod
    async def create_task(session, user_task, user_id) -> dict:
        task_obj = await UserTaskManager.get_task(session=session, task_id=user_task.task_id, user_id=user_id)
        if not task_obj:
            stmt = insert(UserTask).values(user_id=user_id, status=StatusEnum.draft.value, score=0, **user_task.dict())
            return await BaseManager.create_stmt(stmt, session)
        return {"status": 200, "detail": "Already in db"}

    @staticmethod
    async def add_answer(session, task_id, user_id, answer) -> dict:
        user_task = await UserTaskManager.get_task(session=session, task_id=task_id, user_id=user_id)
        task = await TaskManager.get_task(session=session, task_id=task_id)
        data = {
            "task_id": user_task.id,
            "code": answer,
            "func_name": task.func_name,
            "input_data": task.input_data,
            "output_data": task.output_data,
        }
        solution = {
            "status": StatusEnum.draft.value,
            "score": user_task.score,
            "submitted": False,
            "answer": answer,
            "details": ""
        }
        async with aiohttp.ClientSession() as ai_session:
            async with ai_session.post(f'{HOST}solutions/create?token={TOKEN}', json=data) as response:
                res_data = await response.json()
                solution["score"] = res_data["score"]
                if res_data["resolved"]:
                    solution["status"] = StatusEnum.correct.value
                else:
                    solution["status"] = StatusEnum.wrong.value
                    solution["details"] = f"{res_data['error_type']}  -  {res_data['error_value']}"

        stmt = update(UserTask). \
            where(UserTask.task_id == task_id, UserTask.user_id == user_id). \
            values(**solution)
        return await BaseManager.update_stmt(stmt, session)

    @staticmethod
    async def get_solutions(session, user_task_id) -> Optional[List[Solution]]:
        async with aiohttp.ClientSession() as ai_session:
            async with ai_session.get(f'{HOST}solutions/{user_task_id}?token={TOKEN}') as response:
                res_data = await response.json()
        for item in res_data:
            item["status"] = StatusEnum.correct.value if item["resolved"] else StatusEnum.wrong.value
        return res_data

