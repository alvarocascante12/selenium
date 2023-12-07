import allure
import os
import pytest
from automation.selenium.resources.comments_api import CommentsAPI
from automation.selenium.settings.common import *
from automation.selenium.resources.load_json import load_json_data

@allure.feature("API Tests")
@allure.title("Comments API Test")
class TestCommentsAPI:

    @allure.story("GET Comments")
    def test_get_comments(self):
        with allure.step("Initial Setup"):
            comments_api = CommentsAPI()

        with allure.step("Making a GET request"):
            response_get = comments_api.get_comments()

        with allure.step("Verifying the status code"):
            assert response_get.status_code == 200

    @allure.story("POST New Comment")
    def test_post_new_comment(self):
        with allure.step("Initial Setup"):
            comments_api = CommentsAPI()

        with allure.step("Making a POST request"):
            new_comment_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_post = comments_api.create_comment(new_comment_data)

        with allure.step("Verifying the status code"):
            assert response_post.status_code == 201

    @allure.story("PUT Existing Comment")
    def test_put_existing_comment(self):
        with allure.step("Initial Setup"):
            comments_api = CommentsAPI()

        with allure.step("Making a PUT request"):
            comment_id_to_update = 1
            updated_comment_data = load_json_data(DATA_FILES_PATH+"new_post_data.json")
            response_put = comments_api.update_comment(comment_id_to_update, updated_comment_data)

        with allure.step("Verifying the status code"):
            assert response_put.status_code == 200

    @allure.story("DELETE Existing Comment")
    def test_delete_existing_comment(self):
        with allure.step("Initial Setup"):
            comments_api = CommentsAPI()

        with allure.step("Making a DELETE request"):
            comment_id_to_delete = 2
            response_delete = comments_api.delete_comment(comment_id_to_delete)

        with allure.step("Verifying the status code"):
            assert response_delete.status_code == 200

    @allure.story("PATCH Existing Comment")
    def test_patch_existing_comment(self):
        with allure.step("Initial Setup"):
            comments_api = CommentsAPI()

        with allure.step("Making a PATCH request"):
            comment_id_to_patch = 3
            patched_data = {"name": "Patched Name"}
            response_patch = comments_api.patch_comment(comment_id_to_patch, patched_data)

        with allure.step("Verifying the status code"):
            assert response_patch.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__, "--alluredir=./allure-results"])
    os.system("allure serve ./allure-results")