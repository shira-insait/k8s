"""Happy Cat

Revision ID: d175421a42ba
Revises: 786085974ed5
Create Date: 2023-07-30 08:51:45.029194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd175421a42ba'
down_revision = '786085974ed5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('catpic', sa.Column('color', sa.String, server_default='colorful', schema='PUBLIC'))


def downgrade() -> None:
    op.drop_column('catpic', 'color', schema='PUBLIC')