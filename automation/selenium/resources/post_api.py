from .base_api import BaseAPI

class PostsAPI(BaseAPI):
    def get_posts(self):
        return self.get("posts")
    
    def get_post(self, post_id):
        endpoint = f"posts/{post_id}"
        response = self.get(endpoint)
        return response

    def create_post(self, data):
        return self.post("posts", data)

    def update_post(self, post_id, data):
        return self.put(f"posts/{post_id}", data)

    def patch_post(self, post_id, data):
        return self.patch(f"posts/{post_id}", data)

    def delete_post(self, post_id):
        return self.delete(f"posts/{post_id}")