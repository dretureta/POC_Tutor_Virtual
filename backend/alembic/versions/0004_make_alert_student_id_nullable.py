"""Make alert student_id nullable

Revision ID: 0004
Revises: 0003
Create Date: 2024-05-20 15:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '0004'
down_revision = '0003'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('alerts', 'student_id',
               existing_type=UUID(as_uuid=True),
               nullable=True)


def downgrade():
    op.alter_column('alerts', 'student_id',
               existing_type=UUID(as_uuid=True),
               nullable=False)
