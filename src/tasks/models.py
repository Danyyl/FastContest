from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, Boolean, Float

from database import Base, get_async_session
from sqlalchemy.orm import relationship
from tasks.utils import StatusEnum

from utils import ChoiceType


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    text = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    topic = relationship("Topic", backref="tasks")
    score = Column(Integer, nullable=False, default=0)
    tags = relationship("TaskTag", back_populates="task")
    func_name = Column(String, nullable=False)
    input_data = Column(String, nullable=False)
    output_data = Column(String, nullable=False)


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class TaskTag(Base):
    __tablename__ = "task_tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("task.id"))
    task = relationship("Task", back_populates="tags")
    tag_id = Column(Integer, ForeignKey("tag.id"))
    tag = relationship("Tag", backref="tasks")


class UserTask(Base):
    __tablename__ = "user_task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey("task.id"))
    task = relationship("Task", backref="users")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", backref="tasks")
    answer = Column(String, nullable=True)
    status = Column(ChoiceType(
        dict(map(lambda item: (item.name, item.value), StatusEnum))), nullable=False, default=StatusEnum.new.value)
    time = Column(Float, nullable=True)
    details = Column(String, nullable=True)
    score = Column(Integer, nullable=False, default=0)
    submitted = Column(Boolean, nullable=False, default=False)
    submitted_at = Column(TIMESTAMP, default=datetime.utcnow)
