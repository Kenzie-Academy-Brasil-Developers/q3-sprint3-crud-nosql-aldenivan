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

    try:
        return jsonify(get_post), HTTPStatus.OK

    except ValueError:
        return {"msg": "The post don't exist"}, HTTPStatus.NOT_FOUND


def create_post():

    data = request.get_json()
    post = Post(**data)

    post.post_posts()

    Post.serialize_post(post)

    try:
        return jsonify(post.__dict__), HTTPStatus.CREATED

    except AttributeError:
        return {"msg": "Attributes are incorrect"}, HTTPStatus.BAD_REQUEST


def delete_post(id):
    deleted_post = Post.delete_post(id)
    Post.serialize_post(deleted_post)

    try:
        return jsonify(deleted_post), HTTPStatus.OK
    
    except ValueError:
        return {"msg": "The post don't exist"}, HTTPStatus.NOT_FOUND


def update_post(id):

    data = request.get_json()
    update = Post(**data)

    update.update_post(id)
    
    try:
        return jsonify(update.__dict__), HTTPStatus.OK

    except AttributeError:
        return {"msg": "Attributes are incorrect"}, HTTPStatus.BAD_REQUEST

    except ValueError:
        return {"msg": "The post don't exist"}, HTTPStatus.NOT_FOUND
