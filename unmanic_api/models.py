"""Models for Sonarr."""

from dataclasses import dataclass
import datetime
from typing import List

from .exceptions import UnmanicError


@dataclass(frozen=True)
class Worker:
    """
    Object holding worker information from Unmanic.

    Attributes:

    id: The worker id.

    name: The worker name.

    idle: Whether the worker is idle.

    paused: Whether the worker is paused.

    start_time: The start time of the worker.

    current_file: The current file being processed.

    current_task: The current task being processed.
    """

    id: str
    name: str
    idle: bool
    pasued: bool
    start_time: datetime
    current_file: str
    current_task: int

    @staticmethod
    def from_dict(data: dict):
        return Worker(
            id=data.get("id"),
            name=data.get("name"),
            idle=data.get("idle"),
            pasued=data.get("paused"),
            start_time=datetime.datetime.fromtimestamp(int(float(data.get("start_time")))),
            current_file=data.get("current_file"),
            current_task=data.get("current_task"),
        )


@dataclass(frozen=True)
class Settings:
    """
    Object holding settings from Unmanic.

    Attributes:

    ui_port: The port Unmanic is running on.

    config_path: The path to the Unmanic configuration file.

    log_path: The path to the Unmanic log file.

    plugins_path: The path to the Unmanic plugins directory.

    userdata_path: The path to the Unmanic userdata directory.

    debugging: Whether Unmanic is running in debug mode.

    library_path: The path to the Unmanic library directory.

    enabled_library_scanner: Whether the library scanner is enabled.

    schedule_full_scan_minutes: The number of minutes between full library scans.

    follow_symlinks: Whether symlinks are followed when scanning.

    concurrent_file_testers: The number of file testers to run concurrently.

    run_full_scan_on_start: Whether a full library scan is run on startup.

    enable_inotify: Whether inotify is enabled.

    clear_pending_tasks_on_restart: Whether pending tasks are cleared on restart.

    number_of_workers: The number of workers to run.

    cache_path: The path to the Unmanic cache directory.

    installation_name: The name of the Unmanic installation.

    distributed_worker_count_target: The target number of distributed workers.
    """

    ui_port: int
    config_path: str
    log_path: str
    plugins_path: str
    userdata_path: str
    debugging: bool
    library_path: str
    enable_library_scanner: bool
    schedule_full_scan_minutes: int
    follow_symlinks: bool
    concurrent_file_testers: int
    run_full_scan_on_start: bool
    enable_inotify: bool
    clear_pending_tasks_on_restart: bool
    number_of_workers: int
    cache_path: str
    installation_name: str
    distributed_worker_count_target: int

    @staticmethod
    def from_dict(data: dict):
        return Settings(
            ui_port=data.get("ui_port"),
            config_path=data.get("config_path"),
            log_path=data.get("log_path"),
            plugins_path=data.get("plugins_path"),
            userdata_path=data.get("userdata_path"),
            debugging=data.get("debugging"),
            library_path=data.get("library_path"),
            enable_library_scanner=data.get("enable_library_scanner"),
            schedule_full_scan_minutes=data.get("schedule_full_scan_minutes"),
            follow_symlinks=data.get("follow_symlinks"),
            concurrent_file_testers=data.get("concurrent_file_testers"),
            run_full_scan_on_start=data.get("run_full_scan_on_start"),
            enable_inotify=data.get("enable_inotify"),
            clear_pending_tasks_on_restart=data.get(
                "clear_pending_tasks_on_restart"),
            number_of_workers=data.get("number_of_workers"),
            cache_path=data.get("cache_path"),
            installation_name=data.get("installation_name"),
            distributed_worker_count_target=data.get(
                "distributed_worker_count_target"),
        )


class Application:
    """
    Object holding all information of the Unmanic Application.

    Attributes:

    workers: A list of Worker objects.

    settings: A Settings object.

    version: The Unmanic server version.
    """

    settings: Settings
    workers: List[Worker] = []
    version: str

    def __init__(self, data: dict):
        """
        Initialize an empty Unmanic application class.

        Args:

        data: Unmanic API response.
        """
        # Check if all elements are in the passed dict, else raise an Error
        if any(k not in data for k in ["settings", "workers"]):
            raise UnmanicError(
                "Unmanic data is incomplete, cannot construct object")
        self.update_from_dict(data)

    def update_from_dict(self, data: dict) -> "Application":
        """
        Return Application object from Unmanic API response.

        Args:

        data: Unmanic API response.

        Returns:

        Application: Application object.
        """
        if "settings" in data and data["settings"]:
            self.settings = Settings.from_dict(data["settings"])

        if "workers" in data and data["workers"]:
            workers = [Worker.from_dict(worker) for worker in data["workers"]["workers_status"]]
            self.workers = workers

        if "version" in data and data["version"]:
            self.version = data["version"]

        return self
