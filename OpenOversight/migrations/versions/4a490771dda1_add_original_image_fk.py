"""add_original_image_fk

Revision ID: 4a490771dda1
Revises: bd0398fe4aab
Create Date: 2018-06-07 15:32:25.524117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a490771dda1'
down_revision = 'bd0398fe4aab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('faces', sa.Column('fk_face_original_image_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'faces_img_id_fkey', 'faces', type_='foreignkey')
    op.create_foreign_key('fk_face_image_id', 'faces', 'raw_images', ['img_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE', use_alter=True)
    op.create_foreign_key(None, 'faces', 'raw_images', ['fk_face_original_image_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL', use_alter=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'faces', type_='foreignkey')
    op.drop_constraint('fk_face_image_id', 'faces', type_='foreignkey')
    op.create_foreign_key(u'faces_img_id_fkey', 'faces', 'raw_images', ['img_id'], ['id'])
    op.drop_column('faces', 'fk_face_original_image_id')
    # ### end Alembic commands ###
