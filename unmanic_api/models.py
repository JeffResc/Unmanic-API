"""Models for Unmanic."""

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
    paused: bool
    start_time: datetime
    current_file: str
    current_task: int

    @staticmethod
    def from_dict(data: dict):
        return Worker(
            id=data.get("id"),
            name=data.get("name"),
            idle=data.get("idle"),
            paused=data.get("paused"),
            start_time=datetime.datetime.fromtimestamp(
                int(float(data.get("start_time")))),
            current_file=data.get("current_file"),
            current_task=data.get("current_task"),
        )

@dataclass(frozen=True)
class TaskQueue:
    """
    Object holding task queue information from Unmanic.

    Attributes:

    recordsTotal: The total number of records.

    recordsFiltered: The number of records after filtering.

    results: The list of PendingTasks.
    """

    recordsTotal: int
    recordsFiltered: int
    results: List

    @staticmethod
    def from_dict(data: dict):
        return TaskQueue(
            recordsTotal=data.get("recordsTotal"),
            recordsFiltered=data.get("recordsFiltered"),
            results=[PendingTask.from_dict(pending_task) for pending_task in data.get("results")],
        )

@dataclass(frozen=True)
class PendingTask:
    """
    Object holding pending task information from Unmanic.

    Attributes:

    id: The task id.

    abspath: The absolute path of the file.

    priority: The priority of the task.

    type: The type of the task.

    status: The status of the task.
    """

    id: int
    abspath: str
    priority: int
    type: str
    status: str

    @staticmethod
    def from_dict(data: dict):
        return PendingTask(
            id=data.get("id"),
            abspath=data.get("abspath"),
            priority=data.get("priority"),
            type=data.get("type"),
            status=data.get("status"),
        )

@dataclass(frozen=True)
class TaskHistory:
    """
    Object holding task queue information from Unmanic.

    Attributes:

    recordsTotal: The total number of records.

    recordsFiltered: The number of records after filtering.

    results: The list of CompletedTasks.
    """

    recordsTotal: int
    recordsFiltered: int
    results: List

    @staticmethod
    def from_dict(data: dict):
        return TaskHistory(
            recordsTotal=data.get("recordsTotal"),
            recordsFiltered=data.get("recordsFiltered"),
            results=[CompletedTask.from_dict(completed_task) for completed_task in data.get("results")],
        )

@dataclass(frozen=True)
class CompletedTask:
    """
    Object holding completed task information from Unmanic.

    Attributes:

    id: The task id.

    task_label: The task label.

    task_success: Whether the task was successful.

    finish_time: The finish time of the task.
    """

    id: int
    task_label: str
    task_success: bool
    finish_time: datetime

    @staticmethod
    def from_dict(data: dict):
        return CompletedTask(
            id=data.get("id"),
            task_label=data.get("task_label"),
            task_success=data.get("task_success"),
            finish_time=datetime.datetime.fromtimestamp(
                int(float(data.get("finish_time")))),
        )

@dataclass(frozen=True)
class SystemConfiguration:
    """
    Object holding system configurtion from Unmanic.

    Attributes:

    python_version: The python version.

    cpu_info_version_string: The cpu info version string.

    arch: The architecture.

    bits: The bits.

    count: The CPU core count.

    arch_string_raw: The raw architecture string.

    vendor_id_raw: The raw CPU vendor id string.

    brand_raw: The raw CPU brand string.

    hz_advertised_friendly: The advertised CPU frequency.

    hz_actual_friendly: The actual CPU frequency.

    hz_advertised: The advertised CPU frequency.

    hz_actual: The actual CPU frequency.

    stepping: The CPU stepping.

    model: The CPU model.

    family: The CPU family.

    flags: The CPU flags.

    platform: The OS platform.
    """

    python_version: str
    cpu_info_version_string: str
    arch: str
    bits: int
    count: int
    arch_string_raw: str
    vendor_id_raw: str
    brand_raw: str
    hz_advertised_friendly: str
    hz_actual_friendly: str
    hz_advertised: List[int]
    hz_actual: List[int]
    stepping: int
    model: int
    family: int
    flags: List[str]
    platform: List[str]

    @staticmethod
    def from_dict(data: dict):
        return SystemConfiguration(
            python_version=data.get("python"),
            cpu_info_version_string=data.get("devices").get("cpu_info").get("cpu_info_version_string"),
            arch=data.get("devices").get("cpu_info").get("arch"),
            bits=data.get("devices").get("cpu_info").get("bits"),
            count=data.get("devices").get("cpu_info").get("count"),
            arch_string_raw=data.get("devices").get("cpu_info").get("arch_string_raw"),
            vendor_id_raw=data.get("devices").get("cpu_info").get("vendor_id_raw"),
            brand_raw=data.get("devices").get("cpu_info").get("brand_raw"),
            hz_advertised_friendly=data.get("devices").get("cpu_info").get("hz_advertised_friendly"),
            hz_actual_friendly=data.get("devices").get("cpu_info").get("hz_actual_friendly"),
            hz_advertised=data.get("devices").get("cpu_info").get("hz_advertised"),
            hz_actual=data.get("devices").get("cpu_info").get("hz_actual"),
            stepping=data.get("devices").get("cpu_info").get("stepping"),
            model=data.get("devices").get("cpu_info").get("model"),
            family=data.get("devices").get("cpu_info").get("family"),
            flags=data.get("devices").get("cpu_info").get("flags"),
            platform=data.get("devices").get("cpu_info").get("platform"),
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

    enabled_library_scanner: Enable periodic library scans.

    schedule_full_scan_minutes: The number of minutes between full library scans.

    follow_symlinks: Follow symlinks on library scans.

    concurrent_file_testers: The number of file testers to run concurrently.

    run_full_scan_on_start: Run a one off library scan on startup.

    enable_inotify: Enable the library file monitor.

    clear_pending_tasks_on_restart: Clear all pending tasks on startup.

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
