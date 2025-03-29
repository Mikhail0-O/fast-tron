import httpx


async def tron_client(url, address, headers):
    data = {
        'address': address,
        'visible': True
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise httpx.HTTPStatusError(
                message='Ошибка HTTP-ответа!',
                request=response.request,
                response=response,
            )
        result = response.json()
        return result


async def get_balance(url, address, headers):
    result = await tron_client(url, address, headers)
    return result.get('balance', 0)


async def get_energy_and_bandwidth(url, address, headers):
    result = await tron_client(url, address, headers)
    return result.get('EnergyUsed', 0), result.get('NetUsed', 0)
