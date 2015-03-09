"""empty message

Revision ID: 36227aad75b2
Revises: 
Create Date: 2015-03-02 15:51:01.003399

"""

# revision identifiers, used by Alembic.
revision = '36227aad75b2'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'map_point',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('lat', sa.Float(), nullable=False),
        sa.Column('lon', sa.Float(), nullable=False),
        sa.Column('code128', sa.String(length=128), nullable=True),
        sa.Column('hard_id', sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('map_point')
