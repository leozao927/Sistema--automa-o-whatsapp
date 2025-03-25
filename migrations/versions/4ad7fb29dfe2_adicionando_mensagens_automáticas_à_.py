"""Adicionando mensagens automáticas à configuração

Revision ID: 4ad7fb29dfe2
Revises: 
Create Date: 2025-03-20 14:42:27.529163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ad7fb29dfe2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('config_automacao', schema=None) as batch_op:
        batch_op.add_column(sa.Column('saudacoes', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('respostas', sa.JSON(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('palavras_exatas',
               existing_type=sa.TEXT(),
               type_=sa.JSON(),
               existing_nullable=True)
        batch_op.alter_column('palavras_contem',
               existing_type=sa.TEXT(),
               type_=sa.JSON(),
               existing_nullable=True)
        batch_op.drop_column('acompanhamento')

    with op.batch_alter_table('mensagens_salvas', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('chave',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False)

    with op.batch_alter_table('saudacoes', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('email',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('senha',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('senha',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('saudacoes', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('mensagens_salvas', schema=None) as batch_op:
        batch_op.alter_column('chave',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    with op.batch_alter_table('config_automacao', schema=None) as batch_op:
        batch_op.add_column(sa.Column('acompanhamento', sa.TEXT(), nullable=True))
        batch_op.alter_column('palavras_contem',
               existing_type=sa.JSON(),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('palavras_exatas',
               existing_type=sa.JSON(),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
        batch_op.drop_column('respostas')
        batch_op.drop_column('saudacoes')

    # ### end Alembic commands ###
