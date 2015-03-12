"""empty message

Revision ID: 12373524489
Revises: 745b4faa476
Create Date: 2015-03-12 18:05:10.850085

"""

# revision identifiers, used by Alembic.
revision = '12373524489'
down_revision = '745b4faa476'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.rename_table('map_point', 'point')


def downgrade():
    op.rename_table('point', 'map_point')
