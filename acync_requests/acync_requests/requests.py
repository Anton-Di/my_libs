import httpx


async def get(
    url: str,
    headers: dict | None = None,
    params: dict | None = None,
    timeout: int = 5,
) -> dict | str | bytes | None:
    """
    Perform an asynchronous GET request with error handling
    and automatic response type detection.

    Returns:
        - dict: if response is JSON
        - str: if response is text or HTML
        - bytes: for any other content type
        - None: if request failed
    """
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return _parse_response(response)
    except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError):
        return None


async def post(
    url: str,
    data: dict | None = None,
    headers: dict | None = None,
    params: dict | None = None,
    timeout: int = 5,
) -> dict | str | bytes | None:
    """
    Perform an asynchronous POST request with error handling
    and automatic response type detection.

    Returns:
        - dict: if response is JSON
        - str: if response is text or HTML
        - bytes: for any other content type
        - None: if request failed
    """
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(url, json=data, headers=headers, params=params)
            response.raise_for_status()
            return _parse_response(response)
    except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError):
        return None


def _parse_response(response: httpx.Response) -> dict | str | bytes:
    """
    Detect response content type and return appropriate data format.
    """
    content_type = response.headers.get("Content-Type", "").lower()

    if "application/json" in content_type:
        return response.json()
    elif "text" in content_type or "html" in content_type:
        return response.text
    else:
        return response.content