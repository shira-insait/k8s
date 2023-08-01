"""Add adopted column

Revision ID: 786085974ed5
Revises: d46cb0a5092d
Create Date: 2023-07-29 17:30:40.481752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '786085974ed5'
down_revision = 'd46cb0a5092d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('catpic', sa.Column('adopted', sa.Boolean(), nullable=False, server_default=sa.false()), schema='PUBLIC')


def downgrade() -> None:
    op.drop_column('catpic', 'adopted', schema='PUBLIC')