from json import dumps

from fastapi import APIRouter
from aioresponses import aioresponses

from app.clients.async_base_api import AsyncBaseApi


router = APIRouter()
async_base_api = AsyncBaseApi()


@router.get("/simple")
async def simple_get():
    url = "http://localhost:8080/test"
    with aioresponses() as mock_request:
        mock_request.get(url=url, status=200, body=dumps({"succes": 1}))

        response = await async_base_api.get(url=url)
    return response


@router.get("/multi")
async def multi_get():
    url = "http://localhost:8080/test"
    with aioresponses() as mock_request:
        mock_request.get(url=url, status=200, body=dumps({"succes": 1}))
        mock_request.get(url=url, status=200, body=dumps({"succes": 2}))
        mock_request.get(url=url, status=200, body=dumps({"succes": 3}))

        response = []
        response.append(await async_base_api.get(url=url))
        response.append(await async_base_api.get(url=url))
        response.append(await async_base_api.get(url=url))

    return response
