"""Add is_company field ot User model

Revision ID: e8c4698e159d
Revises: 0b0e49b7d102
Create Date: 2024-05-29 21:37:59.679857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8c4698e159d'
down_revision: Union[str, None] = '0b0e49b7d102'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('is_company', sa.Boolean))


def downgrade() -> None:
    op.drop_column('user', 'is_company')
