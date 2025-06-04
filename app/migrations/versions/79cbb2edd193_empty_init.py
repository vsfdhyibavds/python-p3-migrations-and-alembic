"""Empty Init

Revision ID: 79cbb2edd193
Revises: 644266885612
Create Date: 2025-06-04 22:36:45.111611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79cbb2edd193'
down_revision: Union[str, None] = '644266885612'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
