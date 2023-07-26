"""test revision 1

Revision ID: 7c5c4cde7e5e
Revises: d46cb0a5092d
Create Date: 2023-07-26 10:27:38.987263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c5c4cde7e5e'
down_revision = 'd46cb0a5092d'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('catpic', 
    sa.Column('date', sa.Date(), nullable=False), 
    schema='PUBLIC')



def downgrade():
    op.drop_column('catpic', 'date', 
    schema='PUBLIC')
