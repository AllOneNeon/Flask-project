"""empty message

Revision ID: abeddb038354
Revises: c5d95f2c844b
Create Date: 2022-07-29 21:50:36.103470

"""

# revision identifiers, used by Alembic.
revision = 'abeddb038354'
down_revision = 'c5d95f2c844b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('note', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('cyrrency', sa.Enum('BYN', 'RUB', 'USD', 'EUR', name='enum_for_items'), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('selected', sa.Boolean(), nullable=True),
    sa.Column('enquiries_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['enquiries_id'], ['enquiries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###