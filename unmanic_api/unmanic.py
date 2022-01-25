"""Asynchronous Python client for Unmanic."""
from typing import Dict, List, Optional, Type
from aiohttp.client import ClientSession
import json

from .client import Client
from .exceptions import UnmanicError

from .models import (
    Worker,
    Settings,
    PendingTask,
    TaskQueue,
    CompletedTask,
    TaskHistory,
    SystemConfiguration,
)


class Unmanic(Client):
    """
    Main class for Python API.

    Args:

    host: The hostname or IP address of the Unmanic server.

    port: The port number of the Unmanic server.

    base_path: The base path of the API on the Unmanic server.

    request_timeout: The request timeout in seconds.

    session: The aiohttp.ClientSession to use.

    tls: Whether to use TLS.

    verify_ssl: Whether to verify the SSL certificate.

    user_agent: The user agent to use.
    """

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 8888,
        base_path: str = "/unmanic/api/",
        request_timeout: int = 8,
        session: ClientSession = None,
        tls: bool = False,
        verify_ssl: bool = True,
        user_agent: str = None,
    ) -> None:
        """Initilize connection with Unmanic"""
        super().__init__(
            host=host,
            base_path=base_path,
            port=port,
            request_timeout=request_timeout,
            session=session,
            tls=tls,
            verify_ssl=verify_ssl,
            user_agent=user_agent,
        )

    async def get_installation_name(self) -> str:
        """
        Get Unmanic installation name

        Returns:
            str: Unmanic installation name
        """
        try:
            results = await self.get_settings()
            return results.installation_name
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get Unmanic installation name: {e}")
        except:
            raise UnmanicError("Unable to get Unmanic installation name")

    async def get_version(self) -> str:
        """
        Get Unmanic version

        Returns:
            str: Unmanic server version
        """
        results = await self._request("v2/version/read")
        try:
            return results['version']
        except KeyError:
            raise UnmanicError("Unable to get Unmanic version, key not found")
        except TypeError:
            raise UnmanicError("Unable to get Unmanic version, type error, no results")

    async def pause_worker(self, worker_id: str) -> bool:
        """
        Pause a worker

        Args:

        worker_id: The worker id.

        Returns:
            bool: True if successful.
        """
        results = await self._request(f"v2/workers/worker/pause", method='POST', data=json.dumps({"worker_id": worker_id}))
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to pause worker, key not found")
        except TypeError:
            raise UnmanicError("Unable to pause worker, type error, no results")

    async def pause_all_workers(self) -> bool:
        """
        Pause all workers

        Returns:
            bool: True if successful.
        """
        results = await self._request("v2/workers/worker/pause/all", method='POST')
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to pause all workers, key not found")
        except TypeError:
            raise UnmanicError("Unable to pause all workers, type error, no results")

    async def resume_worker(self, worker_id: str) -> bool:
        """
        Resume a worker

        Args:

        worker_id: The worker id.

        Returns:
            bool: True if successful.
        """
        results = await self._request(f"v2/workers/worker/resume", method='POST', data=json.dumps({"worker_id": worker_id}))
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to resume worker, key not found")
        except TypeError:
            raise UnmanicError("Unable to resume worker, type error, no results")

    async def resume_all_workers(self) -> bool:
        """
        Resume all workers

        Returns:
            bool: True if successful.
        """
        results = await self._request("v2/workers/worker/resume/all", method='POST')
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to resume all workers, key not found")
        except TypeError:
            raise UnmanicError("Unable to resume all workers, type error, no results")

    async def terminate_worker(self, worker_id) -> bool:
        """
        Terminate a worker

        Args:

        worker_id: The worker id.

        Returns:
            bool: True if successful.
        """
        results = await self._request("v2/workers/worker/terminate", method='POST', data=json.dumps({"worker_id": worker_id}))
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to terminate worker, key not found")
        except TypeError:
            raise UnmanicError("Unable to terminate worker, type error, no results")

    async def get_workers_status(self) -> List[Worker]:
        """
        Get workers status

        Returns:
            Dict: Workers status
        """
        results = await self._request("v2/workers/status")
        try:
            return [Worker.from_dict(result) for result in results['workers_status']]
        except KeyError:
            raise UnmanicError("Unable to get workers status, key not found")
        except TypeError:
            raise UnmanicError("Unable to get workers status, type error, no results")

    async def get_settings(self) -> Settings:
        """
        Get Unmanic settings

        Returns:
            Dict: Unmanic server settings
        """
        results = await self._request("v2/settings/read")
        try:
            return Settings.from_dict(results['settings'])
        except KeyError:
            raise UnmanicError("Unable to get Unmanic settings, key not found")
        except TypeError:
            raise UnmanicError("Unable to get Unmanic settings, type error, no results")

    async def set_settings(self, settings: Dict) -> bool:
        """
        Set Unmanic settings

        Args:

        settings: The settings to set.

        Returns:
            bool: True if successful.
        """
        results = await self._request("v2/settings/write", method='POST', data=json.dumps({'settings': settings}))
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to set Unmanic settings, key not found")
        except TypeError:
            raise UnmanicError("Unable to set Unmanic settings, type error, no results")

    async def get_workers_count(self) -> int:
        """
        Get workers count

        Returns:
            int: Number of workers
        """
        try:
            results = await self.get_settings()
            return results.number_of_workers
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get worker count: {e}")
        except:
            raise UnmanicError("Unable to get worker count")

    async def set_workers_count(self, number_of_workers: int) -> bool:
        """
        Set workers count

        Args:

        number_of_workers: The number of workers.

        Returns:
            bool: True if successful.
        """
        try:
            return await self.set_settings({'number_of_workers': number_of_workers})
        except UnmanicError as e:
            raise UnmanicError(f"Unable to set worker count: {e}")
        except:
            raise UnmanicError("Unable to set worker count")

    async def trigger_library_scan(self) -> bool:
        """
        Trigger library scan

        Returns:
            bool: True if successful.
        """
        results = await self._request("v1/pending/rescan", method='GET')
        try:
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to trigger library scan, key not found")
        except TypeError:
            raise UnmanicError("Unable to trigger library scan, type error, no results")

    async def get_pending_tasks(self, start=0, length=10, search_value="", order_by="priority", order_direction="desc") -> List[PendingTask]:
        """
        Get pending tasks

        Returns:
            Dict: TaskQueue
        """
        results = await self._request("v2/pending/tasks", method='POST', data=json.dumps({'start': start, 'length': length, 'search_value': search_value, 'order_by': order_by, 'order_direction': order_direction}))
        try:
            return TaskQueue.from_dict(results)
        except TypeError:
            raise UnmanicError("Unable to get pending tasks, type error, no results")

    async def get_task_history(self, start=0, length=10, search_value="", order_by="finish_time", order_direction="desc") -> List[CompletedTask]:
        """
        Get task history

        Returns:
            Dict: TaskHistory
        """
        results = await self._request("v2/history/tasks", method='POST', data=json.dumps({'start': start, 'length': length, 'search_value': search_value, 'order_by': order_by, 'order_direction': order_direction}))
        try:
            return TaskHistory.from_dict(results)
        except TypeError:
            raise UnmanicError("Unable to get task history, type error, no results")

    async def get_system_configuration(self) -> SystemConfiguration:
        """
        Get system configuration

        Returns:
            Dict: SystemConfiguration
        """
        results = await self._request("v2/settings/configuration")
        try:
            return SystemConfiguration.from_dict(results["configuration"])
        except KeyError:
            raise UnmanicError("Unable to get system configuration, key not found")
        except TypeError:
            raise UnmanicError("Unable to get system configuration, type error, no results")

    async def __aenter__(self) -> "Unmanic":
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self.close_session()
