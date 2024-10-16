import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Task


@pytest.fixture
def authenticated_client():
    client = APIClient()
    user = User.objects.create_user(
        "test",
        password="test@?!@#@!aljdfafjjo123")
    client.force_login(user=user)
    return client


@pytest.fixture
def fake_task():
    user = User.objects.get(username="test")
    fakeTask = Task.objects.create(
        title="test title",
        description="test content",
        creator=user,
    )
    return fakeTask


@pytest.mark.django_db
class TestTaskAPI:

    def test_GET_task_list_api_response_200(self, authenticated_client):
        url = reverse("tasks:api-v1:tasks-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200

    def test_POST_task_list_api_response_201(self, authenticated_client):
        url = reverse("tasks:api-v1:tasks-list")
        data = {"title": "string", "description": "string", "done": True}
        response = authenticated_client.post(url, data=data)
        assert response.status_code == 201

    # detail api tests
    # detail api test --- valid responses
    def test_POST_task_list_api_invalid_response_400(self, authenticated_client):
        url = reverse("tasks:api-v1:tasks-list")
        data = {
            "title": "string",
        }
        response = authenticated_client.post(url, data=data)
        assert response.status_code == 400

    def test_GET_task_detail_api_valid_response_200(
        self, authenticated_client, fake_task
    ):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": fake_task.pk})
        response = authenticated_client.get(url)
        assert response.status_code == 200

    def test_PUT_task_detail_valid_response_200(self, authenticated_client, fake_task):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": fake_task.pk})
        response = authenticated_client.put(
            url, data={"title": "edited", "description": "edited", "status": True}
        )
        assert response.status_code == 200

    def test_PATCH_task_detail_valid_response_200(
        self, authenticated_client, fake_task
    ):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": fake_task.pk})
        response = authenticated_client.patch(url, data={"status": True})
        assert response.status_code == 200

    def test_DELETE_task_detail_valid_response_204(
        self, authenticated_client, fake_task
    ):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": fake_task.pk})
        response = authenticated_client.delete(url)
        assert response.status_code == 204

    # detail api test --- invalid responses
    def test_GET_task_detail_api_invalid_response_404(self, authenticated_client):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": 1})
        response = authenticated_client.get(url)
        assert response.status_code == 404

    def test_PUT_task_detail_invalid_response_400(
        self, authenticated_client, fake_task
    ):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": fake_task.pk})
        response = authenticated_client.put(
            url, data={"title": "edited", "status": True}
        )
        assert response.status_code == 400

    def test_PATCH_task_detail_invalid_response_400(
        self, authenticated_client, fake_task
    ):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": fake_task.pk})
        response = authenticated_client.patch(url, data={"title": "a" * 51})
        assert response.status_code == 400

    def test_DELETE_task_detail_invalid_response_204(self, authenticated_client):
        url = reverse("tasks:api-v1:tasks-detail", kwargs={"pk": 1})
        response = authenticated_client.delete(url)
        assert response.status_code == 404
