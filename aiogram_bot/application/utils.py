import aiohttp


async def get_application_by_id(application_id: int) -> dict | None:
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(f"http://192.168.0.102:8000/api/applications/{application_id}/") as response:
            try:
                resp_json = await response.json()
                return resp_json
            except Exception as e:
                print("Error: ", e)
                return {}
