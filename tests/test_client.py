"""Tests for Unmanic-API Client."""
import asyncio

import pytest
from aiohttp import ClientSession, ClientError
from unmanic_api import (
    Client,
    UnmanicBadRequestRequestedEndpointNotFoundError,
    UnmanicBadRequestRequestedMethodNotAllowedError,
    UnmanicBadRequestValidationError,
    UnmanicConnectionError,
    UnmanicError,
    UnmanicInternalServerError,
)

HOST = "192.168.1.99"
PORT = 8888

MATCH_HOST = f"{HOST}:{PORT}"
NON_STANDARD_PORT = 3333


@pytest.mark.asyncio
async def test_json_request(aresponses):
    """Test JSON response is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"version": "0.1.4~655b18b"}',
        ),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        response = await client._request("v2/version/read")
        assert response["version"] == "0.1.4~655b18b"

@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_internal_session(aresponses):
    """Test JSON response is handled correctly with internal session."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"version": "0.1.4~655b18b"}',
        ),
    )

    async with Client(HOST, PORT) as client:
        response = await client._request("v2/version/read")
        assert response["version"] == "0.1.4~655b18b"

@pytest.mark.asyncio
async def test_timeout(aresponses):
    """Test request timeout from the API."""
    # Faking a timeout by sleeping
    async def response_handler(_):
        await asyncio.sleep(2)
        return aresponses.Response(body="Timeout!")

    aresponses.add(MATCH_HOST, "/unmanic/api/v2/version/read", "GET", response_handler)

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session, request_timeout=1)
        with pytest.raises(UnmanicConnectionError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_http_error404(aresponses):
    """Test HTTP 404 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Not Found!", status=404),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicBadRequestRequestedEndpointNotFoundError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_http_error405(aresponses):
    """Test HTTP 405 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Method Not Allowed!", status=405),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicBadRequestRequestedMethodNotAllowedError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_http_error500(aresponses):
    """Test HTTP 500 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Internal Server Error!", status=500),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicInternalServerError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_http_error400(aresponses):
    """Test HTTP 400 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Bad Request!", status=400),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicBadRequestValidationError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_http_error501(aresponses):
    """Test HTTP 501 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Not Implemented!", status=501),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_http_error501_json(aresponses):
    """Test HTTP 501 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Not Implemented!", status=501, headers={"Content-Type": "application/json"}),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            assert await client._request("v2/version/read")

@pytest.mark.asyncio
async def test_request_base_path(aresponses):
    """Test API running on different base path."""
    aresponses.add(
        MATCH_HOST,
        "/my_base_dir/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="GOTCHA!", status=200),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, base_path="/my_base_dir/unmanic/api", session=session)
        response = await client._request("v2/version/read")
        assert response == "GOTCHA!"

@pytest.mark.asyncio
async def test_request_port(aresponses):
    """Test the handling of non-standard API port."""
    aresponses.add(
        f"{HOST}:{NON_STANDARD_PORT}",
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"version": "0.1.4~655b18b"}',
        ),
    )

    async with ClientSession() as session:
        client = Client(
            host=HOST, port=NON_STANDARD_PORT, session=session
        )
        response = await client._request("v2/version/read")
        assert response["version"] == "0.1.4~655b18b"