"""Tests for Sonarr."""
import asyncio

import pytest
from aiohttp import ClientSession

from unmanic_api import Client
from unmanic_api.exceptions import (
    UnmanicBadRequestRequestedEndpointNotFoundError,
    UnmanicBadRequestRequestedMethodNotAllowedError,
    UnmanicBadRequestValidationError,
    UnmanicConnectionError,
    UnmanicError,
    UnmanicInternalServerError,
)

HOST = "10.0.0.2"
PORT = 8888

MATCH_HOST = f"{HOST}:{PORT}"


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
        response = await client._request("version/read")
        assert response["version"] == "0.1.4~655b18b"

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
        response = await client._request("version/read")
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
            assert await client._request("version/read")


@pytest.mark.asyncio
async def test_client_error():
    """Test HTTP client error."""
    async with ClientSession() as session:
        client = Client("#", PORT, session=session)
        with pytest.raises(UnmanicConnectionError):
            assert await client._request("version/read")

@pytest.mark.asyncio
async def test_http_error100(aresponses):
    """Test HTTP 100 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Internal Server Error", status=100),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            assert await client._request("version/read")

@pytest.mark.asyncio
async def test_http_error400_json(aresponses):
    """Test HTTP 400 json response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=400,
            headers={"Content-Type": "application/json"},
            body='{"status": "NOK"}',
        ),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicConnectionError):
            response = await client._request("system/status")
            assert response
            assert response["status"] == "NOK"

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
            assert await client._request("version/read")

@pytest.mark.asyncio
async def test_http_error405_json(aresponses):
    """Test HTTP 405 json response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=405,
            headers={"Content-Type": "application/json"},
            body='{"status": "NOK"}',
        ),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicConnectionError):
            response = await client._request("system/status")
            assert response
            assert response["status"] == "NOK"

@pytest.mark.asyncio
async def test_http_error500(aresponses):
    """Test HTTP 500 response handling."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(text="Internal Server Error", status=500),
    )

    async with ClientSession() as session:
        client = Client(HOST, PORT, session=session)
        with pytest.raises(UnmanicInternalServerError):
            assert await client._request("version/read")