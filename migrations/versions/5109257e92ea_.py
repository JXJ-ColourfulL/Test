"""empty message

Revision ID: 5109257e92ea
Revises: 
Create Date: 2019-03-13 19:59:03.017582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5109257e92ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('u_name', sa.String(length=32), nullable=True),
    sa.Column('_u_password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('u_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_user')
    # ### end Alembic commands ###
