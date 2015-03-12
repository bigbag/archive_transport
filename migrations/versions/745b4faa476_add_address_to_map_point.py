"""add columns carddata to card_track type to map

Revision ID: 745b4faa476
Revises: 16d4ea523799
Create Date: 2015-03-03 13:51:14.354475

"""

# revision identifiers, used by Alembic.
revision = '745b4faa476'
down_revision = '16d4ea523799'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('map_point', sa.Column(
        'address', sa.String(length=256), nullable=True))


def downgrade():
    op.drop_column('map_point', 'address')
