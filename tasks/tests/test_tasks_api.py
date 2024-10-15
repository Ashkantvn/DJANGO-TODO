import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Task


@pytest.fixture
def authenticated_client():
    client = APIClient()
    user = User.objects.create_user("test",password="test@?!@#@!aljdfafjjo123")
    client.force_login(user=user)
    return client

@pytest.mark.django_db
class TestTaskAPI:
    
    def test_get_task_list_api_response_200(self,authenticated_client):
        url = reverse("tasks:api-v1:tasks-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200

    def test_post_task_list_api_response_201(self,authenticated_client):
        url = reverse("tasks:api-v1:tasks-list")
        data = {
            "title": "string",
            "description": "string",
            "done": True
            }
        response = authenticated_client.post(url,data=data)
        assert response.status_code == 201


    def test_post_task_list_api_invalid_response_400(self,authenticated_client):
        url = reverse("tasks:api-v1:tasks-list")
        data = {
            "title": "string",
            }
        response = authenticated_client.post(url,data=data)
        assert response.status_code == 400



    def test_get_task_detail_api_invalid_response_404(self,authenticated_client):
        url = reverse("tasks:api-v1:tasks-detail",kwargs={"pk":1})
        response = authenticated_client.get(url)
        assert response.status_code == 404



    
