"""empty message

Revision ID: 38c3721c0a7
Revises: 36227aad75b2
Create Date: 2015-03-02 15:54:15.802606

"""

# revision identifiers, used by Alembic.
revision = '38c3721c0a7'
down_revision = '36227aad75b2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'card_track',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('blockid', sa.String(length=128), nullable=False),
        sa.Column('cardid', sa.String(length=128), nullable=False),
        sa.Column('time', sa.Integer(), nullable=False),
        sa.Column('lat', sa.Float(), nullable=False),
        sa.Column('lon', sa.Float(), nullable=False),
        sa.Column('status', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('card_track')
