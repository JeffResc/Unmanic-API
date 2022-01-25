"""Tests for Unmanic Interface."""
from typing import List

import pytest
import unmanic_api.models as models
from aiohttp import ClientSession
from unmanic_api import Unmanic, UnmanicError

from . import load_fixture

HOST = "192.168.1.99"
PORT = 8888

MATCH_HOST = f"{HOST}:{PORT}"


@pytest.mark.asyncio
async def test_loop():
    """Test loop usage is handled correctly."""
    async with Unmanic(HOST, PORT) as unmanic:
        assert isinstance(unmanic, Unmanic)

@pytest.mark.asyncio
async def test_get_installation_name(aresponses):
    """Test get_installation_name() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("settings.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_installation_name()

        assert response
        assert response == "Unmanic"

@pytest.mark.asyncio
async def test_get_installation_name_empty_json(aresponses):
    """Test get_installation_name() method is handled correctly given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_installation_name()

@pytest.mark.asyncio
async def test_get_installation_name_empty_string(aresponses):
    """Test get_installation_name() method is handled correctly given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_installation_name()

@pytest.mark.asyncio
async def test_get_pending_tasks(aresponses):
    """Test get_pending_tasks() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/pending/tasks",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("queue.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_pending_tasks()

        assert response
        assert isinstance(response, models.TaskQueue)

        assert response.results[0]
        assert isinstance(response.results[0], models.PendingTask)

@pytest.mark.asyncio
async def test_get_pending_tasks_empty_json(aresponses):
    """Test get_pending_tasks() method is handled correctly given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/pending/tasks",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_pending_tasks()

@pytest.mark.asyncio
async def test_get_pending_tasks_empty_string(aresponses):
    """Test get_pending_tasks() method is handled correctly given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/pending/tasks",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_pending_tasks()

@pytest.mark.asyncio
async def test_get_task_history(aresponses):
    """Test get_task_history() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/history/tasks",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("history.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_task_history()

        assert response
        assert isinstance(response, models.TaskHistory)

        assert response.results[0]
        assert isinstance(response.results[0], models.CompletedTask)

@pytest.mark.asyncio
async def test_get_task_history_empty_json(aresponses):
    """Test get_task_history() method is handled correctly given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/history/tasks",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_task_history()

@pytest.mark.asyncio
async def test_get_task_history_empty_string(aresponses):
    """Test get_task_history() method is handled correctly given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/history/tasks",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_task_history()

@pytest.mark.asyncio
async def test_get_settings(aresponses):
    """Test get_settings() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("settings.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_settings()

        assert response
        assert isinstance(response, models.Settings)

@pytest.mark.asyncio
async def test_get_settings_empty_json(aresponses):
    """Test get_settings() method is handled correctly given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_settings()

@pytest.mark.asyncio
async def test_get_settings_empty_string(aresponses):
    """Test get_settings() method is handled correctly given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_settings()

@pytest.mark.asyncio
async def test_get_system_configuration(aresponses):
    """Test get_system_configuration() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/configuration",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("configuration.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_system_configuration()

        assert response
        assert isinstance(response, models.SystemConfiguration)

@pytest.mark.asyncio
async def test_get_system_configuration_empty_json(aresponses):
    """Test get_system_configuration() method is handled correctly given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/configuration",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_system_configuration()

@pytest.mark.asyncio
async def test_get_system_configuration_empty_string(aresponses):
    """Test get_system_configuration() method is handled correctly given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/configuration",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_system_configuration()

@pytest.mark.asyncio
async def test_get_version(aresponses):
    """Test get_version() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("version.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_version()

        assert response
        assert response == "0.1.4~655b18b"

@pytest.mark.asyncio
async def test_get_version_empty_json(aresponses):
    """Test get_version() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            assert await unmanic.get_version()

@pytest.mark.asyncio
async def test_get_version_empty_string(aresponses):
    """Test get_version() method is handled correctly when given empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/version/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            assert await unmanic.get_version()

@pytest.mark.asyncio
async def test_get_workers_count(aresponses):
    """Test get_worker_count() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("settings.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_workers_count()

        assert response
        assert response == 4

@pytest.mark.asyncio
async def test_get_workers_count_empty_json(aresponses):
    """Test get_worker_count() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_workers_count()

@pytest.mark.asyncio
async def test_get_workers_count_empty_string(aresponses):
    """Test get_worker_count() method is handled correctly when given empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/read",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_workers_count()

@pytest.mark.asyncio
async def test_get_workers_status(aresponses):
    """Test get_workers_status() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixture("workers.json"),
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.get_workers_status()

        assert response
        assert isinstance(response, List)

        assert response[0]
        assert isinstance(response[0], models.Worker)

@pytest.mark.asyncio
async def test_get_workers_status_empty_json(aresponses):
    """Test get_workers_status() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_workers_status()

@pytest.mark.asyncio
async def test_get_workers_status_empty_string(aresponses):
    """Test get_workers_status() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/status",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.get_workers_status()

@pytest.mark.asyncio
async def test_pause_all_workers(aresponses):
    """Test pause_all_workers() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/pause/all",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.pause_all_workers()

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_pause_all_workers_empty_json(aresponses):
    """Test pause_all_workers() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/pause/all",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.pause_all_workers()

@pytest.mark.asyncio
async def test_pause_all_workers_empty_string(aresponses):
    """Test pause_all_workers() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/pause/all",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.pause_all_workers()

@pytest.mark.asyncio
async def test_pause_worker(aresponses):
    """Test pause_worker() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/pause",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.pause_worker("W0")

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_pause_worker_empty_json(aresponses):
    """Test pause_worker() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/pause",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{}',
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.pause_worker("W0")

@pytest.mark.asyncio
async def test_pause_worker_empty_string(aresponses):
    """Test pause_worker() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/pause",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.pause_worker("W0")

@pytest.mark.asyncio
async def test_resume_all_workers(aresponses):
    """Test resume_all_workers() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/resume/all",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.resume_all_workers()

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_resume_all_workers_empty_json(aresponses):
    """Test resume_all_workers() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/resume/all",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.resume_all_workers()

@pytest.mark.asyncio
async def test_resume_all_workers_empty_string(aresponses):
    """Test resume_all_workers() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/resume/all",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.resume_all_workers()

@pytest.mark.asyncio
async def test_resume_worker(aresponses):
    """Test resume_worker() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/resume",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.resume_worker("W0")

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_resume_worker_empty_json(aresponses):
    """Test resume_worker() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/resume",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.resume_worker("W0")

@pytest.mark.asyncio
async def test_resume_worker_empty_string(aresponses):
    """Test resume_worker() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/resume",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.resume_worker("W0")

@pytest.mark.asyncio
async def test_set_settings(aresponses):
    """Test set_settings() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/write",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
        body_pattern='{"settings": {"debugging": true}}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.set_settings({"debugging": True})

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_set_settings_empty_json(aresponses):
    """Test set_settings() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/write",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
        body_pattern='{"settings": {"debugging": true}}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.set_settings({"debugging": True})

@pytest.mark.asyncio
async def test_set_settings_empty_string(aresponses):
    """Test set_settings() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/write",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
        body_pattern='{"settings": {"debugging": true}}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.set_settings({"debugging": True})

@pytest.mark.asyncio
async def test_set_workers_count(aresponses):
    """Test set_workers_count() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/write",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
        body_pattern='{"settings": {"number_of_workers": 4}}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.set_workers_count(4)

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_set_workers_count_empty_json(aresponses):
    """Test set_workers_count() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/write",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True,
        body_pattern='{"settings": {"number_of_workers": 4}}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.set_workers_count(4)

@pytest.mark.asyncio
async def test_set_workers_count_empty_string(aresponses):
    """Test set_workers_count() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/settings/write",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
        body_pattern='{"settings": {"number_of_workers": 4}}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.set_workers_count(4)

@pytest.mark.asyncio
async def test_terminate_worker(aresponses):
    """Test terminate_worker() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/terminate",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.terminate_worker("W0")

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_terminate_worker_empty_json(aresponses):
    """Test terminate_worker() method is handled correctly when given empty json."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/terminate",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{}',
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.terminate_worker("W0")

@pytest.mark.asyncio
async def test_terminate_worker_empty_string(aresponses):
    """Test terminate_worker() method is handled correctly when given an empty string."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v2/workers/worker/terminate",
        "POST",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True,
        body_pattern='{"worker_id": "W0"}',
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.terminate_worker("W0")

@pytest.mark.asyncio
async def test_trigger_library_scan(aresponses):
    """Test trigger_library_scan() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v1/pending/rescan",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{ "success": true }',
        ),
        match_querystring=True
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        response = await unmanic.trigger_library_scan()

        assert response
        assert response == True

@pytest.mark.asyncio
async def test_trigger_library_scan_empty_json(aresponses):
    """Test trigger_library_scan() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v1/pending/rescan",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="{}",
        ),
        match_querystring=True
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.trigger_library_scan()

@pytest.mark.asyncio
async def test_trigger_library_scan_empty_string(aresponses):
    """Test trigger_library_scan() method is handled correctly."""
    aresponses.add(
        MATCH_HOST,
        "/unmanic/api/v1/pending/rescan",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text="",
        ),
        match_querystring=True
    )

    async with ClientSession() as session:
        unmanic = Unmanic(HOST, PORT, session=session)
        with pytest.raises(UnmanicError):
            await unmanic.trigger_library_scan()