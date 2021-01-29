import warnings
import subprocess
from database import *
from flask import Flask, jsonify, request, abort
from flask_cors import CORS


warnings.filterwarnings("ignore")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/v1.0/post', methods=['GET'])
def get_posts():
    result = Post.query.all()
    return jsonify({'item': [post.to_dict() for post in result]}), 201


@app.route('/api/v1.0/post', methods=['POST'])
def create_post():
    post = Post(title=request.json["title"],
                body=request.json["body"], category=request.json["category"])
    db.session.add(post)
    db.commit()
    return jsonify({'item': post.to_dict()}), 201


if __name__ == '__main__':
    app.run(debug=True)
