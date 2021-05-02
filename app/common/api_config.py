from app.clients.async_base_api import AsyncBaseApi

async_base_api = AsyncBaseApi()


async def startup_aiohttp() -> None:
    async_base_api.get_aiohttp_client()


async def shutdown_aiohttp() -> None:
    await async_base_api.close_aiohttp_client()
