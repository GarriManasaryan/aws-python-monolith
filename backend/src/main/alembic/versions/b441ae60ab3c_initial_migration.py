"""Initial migration

Revision ID: b441ae60ab3c
Revises: 
Create Date: 2025-05-20 16:00:15.799210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b441ae60ab3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """create table awspython.public.aw_user(
            id varchar(40) not null,
            name varchar(128) not null,
            primary key(id)
        );
        """
    )


def downgrade() -> None:
    op.execute(
        """
        drop table awspython.public.aw_user;
        """
    )
