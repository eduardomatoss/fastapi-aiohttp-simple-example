from unittest import TestCase

from fastapi.testclient import TestClient

from app.api import app


class ApiTest(TestCase):
    def setUp(self):
        self.client_api = TestClient(app)
        self.response_simple_get = {
            "body": '{"succes": 1}',
            "error": None,
            "status_code": 200,
        }
        self.response_multi_get = [
            {"body": '{"succes": 1}', "error": None, "status_code": 200},
            {"body": '{"succes": 2}', "error": None, "status_code": 200},
            {"body": '{"succes": 3}', "error": None, "status_code": 200},
        ]

    def test_when_I_call_health_check_should_be_success(self):
        response = self.client_api.get("/health-check")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "OK"})

    def test_when_I_call_health_check_using_a_root_path_should_be_success(self):
        response = self.client_api.get("/")
        self.assertEqual(response.status_code, 200)

    def test_when_I_call_endpoint_simple_get_should_be_success(self):
        response = self.client_api.get("/simple")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.response_simple_get)

    def test_when_I_call_endpoint_multi_get_should_be_success(self):
        response = self.client_api.get("/multi")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.response_multi_get)
