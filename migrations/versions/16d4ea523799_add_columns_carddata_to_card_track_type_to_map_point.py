"""add columns carddata to card_track type to map

Revision ID: 16d4ea523799
Revises: 2f0dca12d4bf
Create Date: 2015-03-03 13:51:14.354475

"""

# revision identifiers, used by Alembic.
revision = '16d4ea523799'
down_revision = '2f0dca12d4bf'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('card_track', sa.Column(
        'carddata', sa.String(length=128), nullable=True))
    op.add_column('card_track', sa.Column(
        'start_point', sa.Integer(), nullable=True))
    op.add_column('map_point', sa.Column(
        'type', sa.Integer(), nullable=False, server_default='1'))


def downgrade():
    op.drop_column('card_track', 'carddata')
    op.drop_column('card_track', 'start_point')
    op.drop_column('map_point', 'type')
