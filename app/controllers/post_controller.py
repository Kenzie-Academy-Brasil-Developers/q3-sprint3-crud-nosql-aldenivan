from http.client import CREATED
from turtle import pos
from app.models.post_model import Post
from flask import jsonify, request
from http import HTTPStatus


def retrieve():
    
    post_list = list(Post.get_all())

    Post.serialize_post(post_list)

    return jsonify(post_list), HTTPStatus.OK


def retrieve_one(id):
    get_post = Post.get_one(id)
    Post.serialize_post(get_post)

    return jsonify(get_post), HTTPStatus.OK


def create_post():

    data = request.get_json()
    post = Post(**data)

    post.post_posts()

    Post.serialize_post(post)

    return jsonify(post.__dict__), HTTPStatus.CREATED


def delete_post(id):
    deleted_post = Post.delete_post(id)
    Post.serialize_post(deleted_post)

    return jsonify(deleted_post), HTTPStatus.OK


def update_post(id):

    data = request.get_json()
    post = Post(**data)

    post.update_post(id)
    
    Post.serialize_post(post)

    return jsonify(post.__dict__), HTTPStatus.OK