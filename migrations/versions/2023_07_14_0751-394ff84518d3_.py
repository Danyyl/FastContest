"""empty message

Revision ID: 394ff84518d3
Revises: def2fd0d0ade
Create Date: 2023-07-14 07:51:31.019309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '394ff84518d3'
down_revision = 'def2fd0d0ade'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('func_name', sa.String(), nullable=False))
    op.add_column('task', sa.Column('input_data', sa.String(), nullable=False))
    op.add_column('task', sa.Column('output_data', sa.String(), nullable=False))
    op.add_column('user_task', sa.Column('time', sa.Float(), nullable=True))
    op.add_column('user_task', sa.Column('details', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_task', 'details')
    op.drop_column('user_task', 'time')
    op.drop_column('task', 'output_data')
    op.drop_column('task', 'input_data')
    op.drop_column('task', 'func_name')
    # ### end Alembic commands ###
