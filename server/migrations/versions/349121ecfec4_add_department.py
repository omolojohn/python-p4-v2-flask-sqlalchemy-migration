"""add Department

Revision ID: 349121ecfec4
Revises: 54228817eb42
Create Date: 2024-06-25 18:35:53.011696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '349121ecfec4'
down_revision = '54228817eb42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
