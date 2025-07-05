from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from backend.models import Task
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com", first_name="test", last_name="test", password="test@1234", role="user"
        )
        self.task = Task.objects.create(
            title="Sample Task", description="Sample Description", completed=False
        )

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.client = APIClient()
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

    def test_list_tasks(self):
        response = self.client.get("/api/task/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_retrieve_task(self):
        response = self.client.get(f"/api/task/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)

    def test_create_task_requires_auth(self):
        data = {
            "title": "New Task",
            "description": "Test Description",
            "completed": False
        }
        response = self.client.post("/api/task/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_authenticated(self):
        data = {
            "title": "New Auth Task",
            "description": "Task by auth user",
            "completed": False
        }
        response = self.client.post("/api/task/", data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])

    def test_update_task(self):
        update_data = {
            "title": "Updated Task",
            "description": "Updated Desc",
            "completed": True
        }
        response = self.client.put(f"/api/task/{self.task.id}/", update_data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["completed"])

    def test_delete_task(self):
        response = self.client.delete(f"/api/task/{self.task.id}/", **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
