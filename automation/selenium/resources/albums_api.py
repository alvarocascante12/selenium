from .base_api import BaseAPI

class AlbumsAPI(BaseAPI):
    def get_albums(self):
        return self.get("albums")

    def create_album(self, data):
        return self.post("albums", data)

    def update_album(self, post_id, data):
        return self.put(f"albums/{post_id}", data)

    def patch_album(self, post_id, data):
        return self.patch(f"albums/{post_id}", data)

    def delete_album(self, post_id):
        return self.delete(f"albums/{post_id}")