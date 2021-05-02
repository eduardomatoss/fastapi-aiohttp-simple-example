from json import loads

from aiounittest import AsyncTestCase
from aioresponses import aioresponses
from aiohttp.http_exceptions import HttpBadRequest

from app.clients.async_base_api import AsyncBaseApi


class AsyncBaseApiClientTest(AsyncTestCase):
    def setUp(self):
        self.base_url = "https://postman-echo.com"
        self.default_payload = {"field_1": "value_1", "field_2": "value_2"}
        self.default_response_payload = {"response_id": 100200}
        self.custom_headers = {"Custom Header": "Value of the custom header"}
        self.default_headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "fastapi-aiohttp-simple-example",
        }
        self.api_client = AsyncBaseApi(headers=None, aiohttp_client=None)

    @aioresponses()
    async def test_when_I_call_async_a_get_method_then_should_be_success(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.get(
            self.base_url, status=200, payload=self.default_response_payload
        )
        get_stuff = await self.api_client.get(url=self.base_url)
        await self.api_client.close_aiohttp_client()
        self.assertEqual(get_stuff.get("status_code"), 200)
        self.assertEqual(loads(get_stuff.get("body")), self.default_response_payload)
        self.assertIsNone(get_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_get_method_then_should_be_unsuccess(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.get(self.base_url, exception=HttpBadRequest("Bad Request"))
        get_stuff = await self.api_client.get(url=self.base_url)
        await self.api_client.close_aiohttp_client()
        self.assertIsNone(get_stuff.get("status_code"))
        self.assertIsNone(get_stuff.get("body"))
        self.assertIsNotNone(get_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_post_method_then_should_be_success(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.post(
            self.base_url, status=201, payload=self.default_response_payload
        )
        post_stuff = await self.api_client.post(url=self.base_url, body=self.default_payload)
        await self.api_client.close_aiohttp_client()
        self.assertEqual(loads(post_stuff.get("body")), self.default_response_payload)
        self.assertEqual(post_stuff.get("status_code"), 201)
        self.assertIsNone(post_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_post_method_then_should_be_unsuccess(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.post(self.base_url, exception=HttpBadRequest("Bad Request"))
        post_stuff = await self.api_client.post(url=self.base_url, body=self.default_payload)
        await self.api_client.close_aiohttp_client()
        self.assertIsNotNone(post_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_put_method_then_should_be_success(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.put(
            self.base_url, status=200, payload=self.default_response_payload
        )
        put_stuff = await self.api_client.put(url=self.base_url, body=self.default_payload)
        await self.api_client.close_aiohttp_client()
        self.assertEqual(loads(put_stuff.get("body")), self.default_response_payload)
        self.assertEqual(put_stuff.get("status_code"), 200)
        self.assertIsNone(put_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_put_method_then_should_be_unsuccess(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.put(self.base_url, exception=HttpBadRequest("Bad Request"))
        put_stuff = await self.api_client.put(self.base_url, body=self.default_payload)
        await self.api_client.close_aiohttp_client()
        self.assertIsNotNone(put_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_patch_method_then_should_be_success(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.patch(
            self.base_url, status=200, payload=self.default_response_payload
        )
        patch_stuff = await self.api_client.patch(url=self.base_url, body=self.default_payload)
        await self.api_client.close_aiohttp_client()
        self.assertEqual(loads(patch_stuff.get("body")), self.default_response_payload)
        self.assertEqual(patch_stuff.get("status_code"), 200)
        self.assertIsNone(patch_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_patch_method_then_should_be_unsuccess(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.patch(self.base_url, exception=HttpBadRequest("Bad Request"))
        patch_stuff = await self.api_client.patch(url=self.base_url, body=self.default_payload
        )
        await self.api_client.close_aiohttp_client()
        self.assertIsNotNone(patch_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_delete_method_then_should_be_success(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.delete(f"{self.base_url}/1", status=204)
        delete_stuff = await self.api_client.delete(url=f"{self.base_url}/1")
        await self.api_client.close_aiohttp_client()
        self.assertEqual(delete_stuff.get("status_code"), 204)

    @aioresponses()
    async def test_when_I_call_async_a_delete_method_then_should_be_unsuccess(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.delete(f"{self.base_url}/1", exception=HttpBadRequest("Bad Request"))
        delete_stuff = await self.api_client.delete(url=f"{self.base_url}/1")
        await self.api_client.close_aiohttp_client()
        self.assertIsNotNone(delete_stuff.get("error"))

    @aioresponses()
    async def test_when_I_call_async_a_get_method_then_should_be_an_error(
        self, mock_response
    ):
        self.api_client.get_aiohttp_client()
        mock_response.get(
            self.base_url, status=500, payload=self.default_response_payload
        )
        get_stuff = await self.api_client.get(url=self.base_url)
        await self.api_client.close_aiohttp_client()
        self.assertEqual(get_stuff.get("status_code"), 500)
        self.assertIsNotNone(get_stuff.get("error"))
        self.assertIsNotNone(get_stuff.get("body"))

    def test_when_I_set_a_custom_header_then_should_be_with_all_headers(self):
        api_client_with_custom_headers = AsyncBaseApi(headers=self.custom_headers)
        all_headers = self.default_headers
        all_headers.update(self.custom_headers)
        self.assertDictEqual(all_headers, api_client_with_custom_headers.headers)

    def test_when_I_call_add_custom_header_then_should_be_with_all_headers(self):
        api_client_with_custom_headers = AsyncBaseApi(headers=self.custom_headers)

        custom_test_header = {"custom_test_header": "custom_test_value"}
        api_client_with_custom_headers.add_custom_header(
            "custom_test_header", "custom_test_value"
        )

        all_headers = self.default_headers
        all_headers.update(self.custom_headers)
        all_headers.update(custom_test_header)
        self.assertDictEqual(all_headers, api_client_with_custom_headers.headers)

    def test_when_I_call_clear_custom_headera_then_should_be_default_headers(self):
        api_client_with_custom_headers = AsyncBaseApi(headers=self.custom_headers)
        api_client_with_custom_headers.add_custom_header(
            "custom_test_header", "custom_test_value"
        )
        api_client_with_custom_headers.clear_custom_headers()

        self.assertDictEqual(
            self.default_headers, api_client_with_custom_headers.headers
        )

    @aioresponses()
    async def test_when_I_call_async_a_get_and_has_no_response_should_be_success(
        self, mock_response
    ):
        dict_to_test = {"status_code": 0, "body": "", "error": None}
        await self.api_client.close_aiohttp_client()
        self.api_client.get_aiohttp_client()
        mock_response.get(self.base_url, status=0)
        response = await self.api_client.get(url=self.base_url)
        await self.api_client.close_aiohttp_client()
        self.assertDictEqual(response, dict_to_test)
