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

    if(get_post == None):
        raise FileNotFoundError

    return jsonify(get_post), HTTPStatus.OK
    

def create_post():

    data = request.get_json()
    post = Post(**data)

    post.post_posts()

    Post.serialize_post(post)

    return jsonify(post.__dict__), 201


def delete_post(id):
    deleted_post = Post.delete_post(id)
    Post.serialize_post(deleted_post)
  
    if(deleted_post == None):
        raise FileNotFoundError

    return jsonify(deleted_post), HTTPStatus.OK
   

def update_post(id):

    data = request.get_json()
    updated_post = Post(**data)

    updated_post.update_post(id)
    
    if (Post.checking_id_exist(id) == None):
        raise FileNotFoundError
    
    return jsonify(updated_post.__dict__), HTTPStatus.OK

