from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, server_default=db.func.now())
    updated_date = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    status = db.Column(db.String(100), nullable=False)
