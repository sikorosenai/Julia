"""User model - add column creation_date

Revision ID: 9dd2bd8b6d36
Revises: 3f1c54be843f
Create Date: 2023-02-10 18:37:42.158886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dd2bd8b6d36'
down_revision = '3f1c54be843f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creation_date', sa.DateTime(timezone=True), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('creation_date')

    # ### end Alembic commands ###
