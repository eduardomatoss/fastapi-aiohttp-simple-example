from unittest import TestCase

from fastapi.testclient import TestClient

from app.api import app


class ApiTest(TestCase):
    def setUp(self):
        self.client_api = TestClient(app)

    def test_when_I_call_health_check_should_be_success(self):
        response = self.client_api.get("/health-check")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "OK"})

    def test_when_I_call_health_check_using_a_root_path_should_be_success(self):
        response = self.client_api.get("/")
        self.assertEqual(response.status_code, 200)
