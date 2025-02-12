from flask import Blueprint, request, jsonify
from models import db, Post
from schemas import post_schema, posts_schema

api = Blueprint("api", __name__)

@api.route("/article/", methods=["POST"])
def add_article():
    data = request.json

    if data["status"] not in ["Publish", "Draft", "Trash"]:
        return jsonify({"error": "Invalid status"}), 400

    new_post = Post(
        title=data["title"],
        content=data["content"],
        category=data["category"],
        status=data["status"]
    )
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Article added successfully"}), 201

@api.route("/article", methods=["GET"])
def get_articles():
    posts = Post.query.all()
    return jsonify([{
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "status": post.status
    } for post in posts])

@api.route("/article/<int:id>", methods=["GET"])
def get_article(id):
    post = Post.query.get(id)
    if not post:
        return jsonify({"error": "Article not found"}), 404
    
    return jsonify({
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "category": post.category,
        "status": post.status
    })

@api.route("/article/<int:id>", methods=["PUT"])
def update_article(id):
    post = Post.query.get(id)
    if post:
        data = request.json
        for key, value in data.items():
            setattr(post, key, value)
        db.session.commit()
        return post_schema.jsonify(post), 200
    return jsonify({"error": "Article not found"}), 404

@api.route("/article/<int:id>", methods=["DELETE"])
def delete_article(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return jsonify({"message": "Article deleted"}), 200
    return jsonify({"error": "Article not found"}), 404



