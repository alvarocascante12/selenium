from .base_api import BaseAPI

class CommentsAPI(BaseAPI):
    def get_comments(self):
        return self.get("comments")

    def create_comment(self, data):
        return self.post("comments", data)

    def update_comment(self, post_id, data):
        return self.put(f"comments/{post_id}", data)

    def patch_comment(self, post_id, data):
        return self.patch(f"comments/{post_id}", data)

    def delete_comment(self, post_id):
        return self.delete(f"comments/{post_id}")