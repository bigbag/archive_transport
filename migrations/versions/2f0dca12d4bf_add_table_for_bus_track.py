"""empty message

Revision ID: 2f0dca12d4bf
Revises: 38c3721c0a7
Create Date: 2015-03-02 15:56:17.486386

"""

# revision identifiers, used by Alembic.
revision = '2f0dca12d4bf'
down_revision = '38c3721c0a7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'bus_track',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('blockid', sa.String(length=128), nullable=False),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.Column('lat', sa.Float(), nullable=False),
        sa.Column('lon', sa.Float(), nullable=False),
        sa.Column('event', sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('bus_track')
