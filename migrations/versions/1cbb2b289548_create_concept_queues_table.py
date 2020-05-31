"""create concept_queues table

Revision ID: 1cbb2b289548
Revises: a0a8a1fbcb5e
Create Date: 2020-05-30 18:42:08.288327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cbb2b289548'
down_revision = 'a0a8a1fbcb5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('concept_queues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('actualClientId', sa.Integer(), nullable=True),
    sa.Column('ownerId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actualClientId'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['ownerId'], ['owners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_concept_queues_name'), 'concept_queues', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_concept_queues_name'), table_name='concept_queues')
    op.drop_table('concept_queues')
    # ### end Alembic commands ###
