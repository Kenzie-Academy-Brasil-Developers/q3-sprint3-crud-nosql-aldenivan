from app.controllers import post_controller

def post_route(app):

    @app.get("/posts")
    def read_posts():
        return post_controller.retrieve()


    @app.get("/posts/<int:id>")
    def read_post_by_id(id):    
        return post_controller.retrieve_one(id)    
    

    @app.post("/posts")
    def create_post():
        return post_controller.create_post()
        

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return post_controller.delete_post(id)    


    @app.patch("/posts/<int:id>")
    def update_post(id):
        return post_controller.update_post(id)