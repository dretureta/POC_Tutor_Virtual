"""Add role to user

Revision ID: 0005
Revises: 0004
Create Date: 2024-05-21 16:10:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0005'
down_revision = '0004'
branch_labels = None
depends_on = None


def upgrade():
    # Create the ENUM type
    user_role = sa.Enum('admin', 'teacher', name='userrole')
    user_role.create(op.get_bind(), checkfirst=True)

    # Add the column to the table
    op.add_column('users', sa.Column('role', user_role, nullable=False, server_default='teacher'))


def downgrade():
    op.drop_column('users', 'role')

    # Drop the ENUM type
    user_role = sa.Enum('admin', 'teacher', name='userrole')
    user_role.drop(op.get_bind())
