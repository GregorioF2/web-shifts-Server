"""add unique constraint to users name

Revision ID: fe0535c434b5
Revises: 0f42ecbc1e99
Create Date: 2020-06-13 17:35:35.890116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe0535c434b5'
down_revision = '0f42ecbc1e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_name', table_name='users')
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.create_index('ix_users_name', 'users', ['name'], unique=False)
    # ### end Alembic commands ###
