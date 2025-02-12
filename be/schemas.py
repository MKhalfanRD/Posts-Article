from flask_marshmallow import Marshmallow
from models import Post

ma = Marshmallow()

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
