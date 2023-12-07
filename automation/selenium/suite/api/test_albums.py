import allure
import os
import pytest
from automation.selenium.resources.albums_api import AlbumsAPI
from automation.selenium.settings.common import *
from automation.selenium.resources.load_json import load_json_data

@allure.feature("API Tests")
@allure.title("Albums API Test")
class TestAlbumsAPI:

    @allure.story("GET Albums")
    def test_get_albums(self):
        with allure.step("Initial Setup"):
            albums_api = AlbumsAPI()

        with allure.step("Making a GET request"):
            response_get = albums_api.get_albums()

        with allure.step("Verifying the status code"):
            assert response_get.status_code == 200

    @allure.story("POST New Album")
    def test_post_new_album(self):
        with allure.step("Initial Setup"):
            albums_api = AlbumsAPI()

        with allure.step("Making a POST request"):
            new_album_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_post = albums_api.create_album(new_album_data)

        with allure.step("Verifying the status code"):
            assert response_post.status_code == 201

    @allure.story("PUT Existing Album")
    def test_put_existing_album(self):
        with allure.step("Initial Setup"):
            albums_api = AlbumsAPI()

        with allure.step("Making a PUT request"):
            album_id_to_update = 1
            updated_album_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_put = albums_api.update_album(album_id_to_update, updated_album_data)

        with allure.step("Verifying the status code"):
            assert response_put.status_code == 200

    @allure.story("DELETE Existing Album")
    def test_delete_existing_album(self):
        with allure.step("Initial Setup"):
            albums_api = AlbumsAPI()

        with allure.step("Making a DELETE request"):
            album_id_to_delete = 2
            response_delete = albums_api.delete_album(album_id_to_delete)

        with allure.step("Verifying the status code"):
            assert response_delete.status_code == 200

    @allure.story("PATCH Existing Album")
    def test_patch_existing_album(self):
        with allure.step("Initial Setup"):
            albums_api = AlbumsAPI()

        with allure.step("Making a PATCH request"):
            album_id_to_patch = 3
            patched_data = {"title": "Patched Album Title"}
            response_patch = albums_api.patch_album(album_id_to_patch, patched_data)

        with allure.step("Verifying the status code"):
            assert response_patch.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "--alluredir=./allure-results"])
    os.system("allure serve ./allure-results")
