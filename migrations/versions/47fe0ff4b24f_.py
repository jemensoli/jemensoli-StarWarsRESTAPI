"""empty message

Revision ID: 47fe0ff4b24f
Revises: 8c755e4046fb
Create Date: 2023-10-28 03:42:10.946272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47fe0ff4b24f'
down_revision = '8c755e4046fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('species', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.Column('birthYear', sa.String(length=250), nullable=False),
    sa.Column('height', sa.String(length=250), nullable=False),
    sa.Column('mass', sa.String(length=250), nullable=False),
    sa.Column('hairColor', sa.String(length=250), nullable=False),
    sa.Column('eyeColor', sa.String(length=250), nullable=False),
    sa.Column('skinColor', sa.String(length=250), nullable=False),
    sa.Column('films', sa.String(length=250), nullable=False),
    sa.Column('created', sa.String(length=250), nullable=False),
    sa.Column('edited', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('surfaceWater', sa.String(length=250), nullable=False),
    sa.Column('rotationPeriod', sa.String(length=250), nullable=False),
    sa.Column('orbitalPeriod', sa.String(length=250), nullable=False),
    sa.Column('gravity', sa.String(length=250), nullable=False),
    sa.Column('films', sa.String(length=250), nullable=False),
    sa.Column('created', sa.String(length=250), nullable=False),
    sa.Column('edited', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('type', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(length=250), nullable=False),
    sa.Column('manufactured', sa.String(length=250), nullable=False),
    sa.Column('length', sa.String(length=250), nullable=False),
    sa.Column('consumables', sa.String(length=250), nullable=False),
    sa.Column('speed', sa.String(length=250), nullable=False),
    sa.Column('cost', sa.String(length=250), nullable=False),
    sa.Column('capacity', sa.String(length=250), nullable=False),
    sa.Column('crew', sa.String(length=250), nullable=False),
    sa.Column('passengers', sa.String(length=250), nullable=False),
    sa.Column('films', sa.String(length=250), nullable=False),
    sa.Column('created', sa.String(length=250), nullable=False),
    sa.Column('edited', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('characters_id', sa.Integer(), nullable=True),
    sa.Column('planets_id', sa.Integer(), nullable=True),
    sa.Column('vehicles_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['characters_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicles_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=80), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    op.drop_table('favorites')
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
