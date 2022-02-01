from app.controllers import post_controller

def post_route(app):

    @app.get("/posts")
    def read_posts():
        return post_controller.retrieve()


    @app.get("/posts/<int:id>")
    def read_post_by_id(id):    

        try:
            return post_controller.retrieve_one(id)    

        except FileNotFoundError:
            return {"msg": "The post don't exist"}, 404

    @app.post("/posts")
    def create_post():

        try:
            return post_controller.create_post()
        
        except KeyError:
            return {"msg": "Attributes are incorrect"}, 400    
        

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        
        try:
            return post_controller.delete_post(id)    

        except FileNotFoundError:
            return {"msg": "The post don't exist"}, 404


    @app.patch("/posts/<int:id>")
    def update_post(id):

        try:
            return post_controller.update_post(id)
        
        except KeyError:
            return {"msg": "Attributes are incorrect"}, 400  
       
        except FileNotFoundError:
            return {"msg": "The post don't exist"}, 404