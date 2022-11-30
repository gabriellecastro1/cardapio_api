"""empty message

Revision ID: 0c4bc6a01253
Revises: 23e7d741b19f
Create Date: 2022-11-30 08:22:51.863395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c4bc6a01253'
down_revision = '23e7d741b19f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('matricula', sa.String(length=20), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('matricula')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aluno')
    # ### end Alembic commands ###