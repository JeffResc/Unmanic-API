"""Asynchronous Python client for Unmanic."""
from typing import Dict, List, Optional
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
        except UnmanicError as e:
            raise UnmanicError(f"Unable to pause all workers: {e}")
        except:
            raise UnmanicError("Unable to get Unmanic version")

    async def pause_worker(self, worker_id: str) -> bool:
        """
        Pause a worker

        Args:

        worker_id: The worker id.

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request(f"v2/workers/worker/pause", method='POST', data=json.dumps({"worker_id": worker_id}))
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to pause worker, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to pause worker: {e}")
        except:
            raise UnmanicError("Unable to pause worker")

    async def pause_all_workers(self) -> bool:
        """
        Pause all workers

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request("v2/workers/worker/pause/all", method='POST')
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to pause all workers, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to pause all workers: {e}")
        except:
            raise UnmanicError("Unable to pause all workers")

    async def resume_worker(self, worker_id: str) -> bool:
        """
        Resume a worker

        Args:

        worker_id: The worker id.

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request(f"v2/workers/worker/resume", method='POST', data=json.dumps({"worker_id": worker_id}))
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to resume worker, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to resume worker: {e}")
        except:
            raise UnmanicError("Unable to resume worker")

    async def resume_all_workers(self) -> bool:
        """
        Resume all workers

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request("v2/workers/worker/resume/all", method='POST')
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to resume all workers, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to resume all workers: {e}")
        except:
            raise UnmanicError("Unable to resume all workers")

    async def terminate_worker(self, worker_id) -> bool:
        """
        Terminate a worker

        Args:

        worker_id: The worker id.

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request("v2/workers/worker/terminate", method='POST', data=json.dumps({"worker_id": worker_id}))
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to terminate worker, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to terminate worker: {e}")
        except:
            raise UnmanicError("Unable to terminate worker")

    async def get_workers_status(self) -> List[Worker]:
        """
        Get workers status

        Returns:
            Dict: Workers status
        """
        try:
            results = await self._request("v2/workers/status")
            return [Worker.from_dict(result) for result in results['workers_status']]
        except KeyError:
            raise UnmanicError("Unable to get workers status, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get workers status: {e}")

    async def get_settings(self) -> Settings:
        """
        Get Unmanic settings

        Returns:
            Dict: Unmanic server settings
        """
        try:
            results = await self._request("v2/settings/read")
            return Settings.from_dict(results['settings'])
        except KeyError:
            raise UnmanicError("Unable to get Unmanic settings, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get Unmanic settings: {e}")
        except:
            raise UnmanicError("Unable to get Unmanic settings")

    async def set_settings(self, settings: Dict) -> bool:
        """
        Set Unmanic settings

        Args:

        settings: The settings to set.

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request("v2/settings/write", method='POST', data=json.dumps({'settings': settings}))
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to set Unmanic settings, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to set Unmanic settings: {e}")
        except:
            raise UnmanicError("Unable to set Unmanic settings")

    async def get_workers_count(self) -> int:
        """
        Get workers count

        Returns:
            int: Number of workers
        """
        try:
            results = await self.get_settings()
            return results.number_of_workers
        except KeyError:
            raise UnmanicError("Unable to get workers count, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get workers count: {e}")
        except:
            raise UnmanicError("Unable to get workers count")

    async def set_workers_count(self, number_of_workers: int) -> bool:
        """
        Set workers count

        Args:

        number_of_workers: The number of workers.

        Returns:
            bool: True if successful.
        """
        try:
            results = await self.set_settings({'number_of_workers': number_of_workers})
            return results
        except KeyError:
            raise UnmanicError("Unable to set workers count, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to set workers count: {e}")
        except:
            raise UnmanicError("Unable to set workers count")

    async def trigger_library_scan(self) -> bool:
        """
        Trigger library scan

        Returns:
            bool: True if successful.
        """
        try:
            results = await self._request("v1/pending/rescan", method='GET')
            return results['success']
        except KeyError:
            raise UnmanicError("Unable to trigger library scan, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to trigger library scan: {e}")
        except:
            raise UnmanicError("Unable to trigger library scan")

    async def get_pending_tasks(self, start=0, length=10, search_value="", order_by="priority", order_direction="desc") -> List[PendingTask]:
        """
        Get pending tasks

        Returns:
            Dict: TaskQueue
        """
        try:
            results = await self._request("v2/pending/tasks", method='POST', data=json.dumps({'start': start, 'length': length, 'search_value': search_value, 'order_by': order_by, 'order_direction': order_direction}))
            return TaskQueue.from_dict(results)
        except KeyError:
            raise UnmanicError("Unable to get pending tasks, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get pending tasks: {e}")
        except:
            raise UnmanicError("Unable to get pending tasks")

    async def get_task_history(self, start=0, length=10, search_value="", order_by="finish_time", order_direction="desc") -> List[CompletedTask]:
        """
        Get task history

        Returns:
            Dict: TaskHistory
        """
        try:
            results = await self._request("v2/history/tasks", method='POST', data=json.dumps({'start': start, 'length': length, 'search_value': search_value, 'order_by': order_by, 'order_direction': order_direction}))
            return TaskHistory.from_dict(results)
        except KeyError:
            raise UnmanicError("Unable to get task history, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get task history: {e}")
        except:
            raise UnmanicError("Unable to get task history")

    async def get_system_configuration(self) -> SystemConfiguration:
        """
        Get system configuration

        Returns:
            Dict: SystemConfiguration
        """
        try:
            results = await self._request("v2/settings/configuration")
            return SystemConfiguration.from_dict(results["configuration"])
        except KeyError:
            raise UnmanicError("Unable to get system configuration, key not found")
        except UnmanicError as e:
            raise UnmanicError(f"Unable to get system configuration: {e}")
        except:
            raise UnmanicError("Unable to get system configuration")

    async def __aenter__(self) -> "Unmanic":
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info) -> None:
        """Async exit."""
        await self.close_session()
