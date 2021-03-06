"""followers

Revision ID: 76abb3f9221d
Revises: 7075b3ba5894
Create Date: 2020-01-07 10:25:14.055545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76abb3f9221d'
down_revision = '7075b3ba5894'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
