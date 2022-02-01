from tabnanny import check
import pymongo
from bson.objectid import ObjectId
from app.services.posts_services import creating_id


client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["kenzie"]


class Post:

    def __init__(self, **kwargs) -> None:
        self.author = kwargs["author"]
        self.content = kwargs["content"]
        self.tags = kwargs["tags"]
        self.title = kwargs["title"]
        self.created_at = {}
        self.updated_at = {}

    def post_posts(self):
        self.id = creating_id(list(db.posts.find()))
        self.created_at["create_day"] = (ObjectId().generation_time.today())
        self.updated_at = {"last_update": (ObjectId().generation_time.today())}
        db.posts.insert_one(self.__dict__)

    def update_post(self, post_id):
        
        update_author = self.__dict__["author"]
        update_content = self.__dict__["content"]
        update_tags = self.__dict__["tags"]
        update_title = self.__dict__["title"]
        update_time = self.updated_at = {"last_update": (ObjectId().generation_time.today())}

        update_post = db.posts.update_one({"id": post_id}, {"$set": {"author": update_author, "content": update_content, "tags": update_tags, "title": update_title, "updated_at": update_time}})

        return update_post

    @staticmethod
    def get_all():
        
        post_list = db.posts.find()

        return post_list

    @staticmethod
    def get_one(post_id):
    
        post = db.posts.find_one({"id": post_id})

        return post

    @staticmethod
    def serialize_post(data):

        if type(data) is list:
            for post in data:
                post.pop("_id")

        elif type(data) is Post:
            
            data._id = str(data._id)
           
        elif type(data) is dict:
            data.pop("_id")

    @staticmethod
    def delete_post(post_id):

        deleted_post = db.posts.find_one_and_delete({"id": post_id})

        return deleted_post

    @staticmethod
    def checking_id_exist(id):

        check = db.post.find_one({"id": id})