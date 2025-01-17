"""initial migration

Revision ID: ea5a84482dcc
Revises: 
Create Date: 2024-08-03 12:37:50.979308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea5a84482dcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('publish_year', sa.Integer(), nullable=True),
    sa.Column('page', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('summary', sa.String(), nullable=True),
    sa.Column('star', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('loans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_date', sa.Date(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('returned_date', sa.Date(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('loan_date < returned_date', name='check_loan_date_before_returned_date'),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_loans_book_id_books')),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], name=op.f('fk_loans_member_id_members')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loans')
    op.drop_table('members')
    op.drop_table('books')
    # ### end Alembic commands ###
