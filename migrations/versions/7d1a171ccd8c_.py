"""empty message

Revision ID: 7d1a171ccd8c
Revises: 
Create Date: 2021-03-23 10:42:08.644539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d1a171ccd8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('numberOfBedrooms', sa.Integer(), nullable=True),
    sa.Column('numberOfBathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('ptype', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('photoFilename', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_info')
    # ### end Alembic commands ###
