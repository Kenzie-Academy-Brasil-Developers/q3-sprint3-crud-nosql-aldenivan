from turtle import pos
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["kenzie"]


class Post:
    def __init__(self, **kwargs) -> None:
        self.author = kwargs["author"]
        self.content = kwargs["content"]
        self.tags = kwargs["tags"]
        self.title = kwargs["title"]


    def post_posts(self):
        db.posts.insert_one(self.__dict__)

    def update_post(self, post_id):
        
        updated_post = db.posts.find_one_and_update({"id": post_id}, {"$inc": {"content": self.content}})

        return updated_post

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

        post_id = 0
        length_list = len(list(db.posts.find()))
        
        if type(data) is list:
            for post in data:
                post.update({"_id": str(post["_id"])})
                
                if post.get("id") == None:
                    
                    if( length_list > post_id):
                        db.posts.update_one({"_id": post["_id"]}, {"$inc": {"id": (length_list)}})
                        post_id = length_list

                    else:
                        post_id += 1   
                        db.posts.update_one({"_id": post["_id"]}, {"$inc": {"id": (post_id)}})


        elif type(data) is Post:
            data._id = str(data._id)

            if( length_list > post_id):
                data.id = len(list(db.posts.find()))
                post_id = data.id
        
            else:
                post_id += 1
                data.id = post_id


        elif type(data) is dict:
            data.update({"_id": str(data["_id"])})
            print(data)


    @staticmethod
    def delete_post(post_id):

        deleted_post = db.posts.find_one_and_delete({"id": post_id})

        return deleted_post

    