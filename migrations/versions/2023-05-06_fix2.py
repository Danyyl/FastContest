"""fix2

Revision ID: a18c344e4ecc
Revises: 30b25e85dba7
Create Date: 2023-05-06 01:28:52.441589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a18c344e4ecc'
down_revision = '826963568097'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('topic_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'topic', ['topic_id'], ['id'])
    op.add_column('task_tag', sa.Column('task_id', sa.Integer(), nullable=True))
    op.add_column('task_tag', sa.Column('tag_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task_tag', 'task', ['task_id'], ['id'])
    op.create_foreign_key(None, 'task_tag', 'tag', ['tag_id'], ['id'])
    op.add_column('user_task', sa.Column('task_id', sa.Integer(), nullable=True))
    op.add_column('user_task', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_task', 'task', ['task_id'], ['id'])
    op.create_foreign_key(None, 'user_task', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_task', type_='foreignkey')
    op.drop_constraint(None, 'user_task', type_='foreignkey')
    op.drop_column('user_task', 'user_id')
    op.drop_column('user_task', 'task_id')
    op.drop_constraint(None, 'task_tag', type_='foreignkey')
    op.drop_constraint(None, 'task_tag', type_='foreignkey')
    op.drop_column('task_tag', 'tag_id')
    op.drop_column('task_tag', 'task_id')
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'topic_id')
    # ### end Alembic commands ###
