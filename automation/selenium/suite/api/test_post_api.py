import allure
import os
import pytest
from automation.selenium.resources.post_api import PostsAPI
from automation.selenium.settings.common import *
from automation.selenium.resources.load_json import load_json_data

@allure.feature("API Tests")
@allure.title("Posts API Test")
class TestPostsAPI:

    @allure.story("GET Posts")
    def test_get_posts(self):
        with allure.step("Initial Setup"):
            posts_api = PostsAPI()

        with allure.step("Making a GET request"):
            response_get = posts_api.get_posts()

        with allure.step("Verifying the status code"):
            assert response_get.status_code == 200

    @allure.story("POST New Post")
    def test_post_new_post(self):
        with allure.step("Initial Setup"):
            posts_api = PostsAPI()

        with allure.step("Making a POST request"):
            new_post_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_post = posts_api.create_post(new_post_data)

        with allure.step("Verifying the status code"):
            assert response_post.status_code == 201

    @allure.story("GET New Post")
    def test_get_new_post(self):
        with allure.step("Initial Setup"):
            posts_api = PostsAPI()

        with allure.step("Making a GET request for the new post"):
            response_get_new_post = posts_api.get_post(100)

        with allure.step("Verifying the status code"):
            assert response_get_new_post.status_code == 200

        with allure.step("Verifying the details of the new post"):
            new_post = response_get_new_post.json()
            new_post_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            assert new_post["title"] == new_post_data["title"]
            assert new_post["body"] == new_post_data["body"]

    @allure.story("PUT Existing Post")
    def test_put_existing_post(self):
        with allure.step("Initial Setup"):
            posts_api = PostsAPI()

        with allure.step("Making a PUT request"):
            post_id_to_update = 1
            new_post_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_put = posts_api.update_post(post_id_to_update, new_post_data)

        with allure.step("Verifying the status code"):
            assert response_put.status_code == 200

    @allure.story("DELETE Existing Post")
    def test_delete_existing_post(self):
        with allure.step("Initial Setup"):
            posts_api = PostsAPI()

        with allure.step("Making a DELETE request"):
            post_id_to_delete = 2
            response_delete = posts_api.delete_post(post_id_to_delete)

        with allure.step("Verifying the status code"):
            assert response_delete.status_code == 200

    @allure.story("PATCH Existing Post")
    def test_patch_existing_post(self):
        with allure.step("Initial Setup"):
            posts_api = PostsAPI()

        with allure.step("Making a PATCH request"):
            post_id_to_patch = 3
            new_post_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_patch = posts_api.patch_post(post_id_to_patch, new_post_data)

        with allure.step("Verifying the status code"):
            assert response_patch.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "--alluredir=./allure-results"])
    os.system("allure serve ./allure-results")
