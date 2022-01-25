"""Tests for Unmanic-API Models."""
import json

import unmanic_api.models as models
from unmanic_api import UnmanicError

from . import load_fixture

QUEUE = json.loads(load_fixture("queue.json"))
SETTINGS = json.loads(load_fixture("settings.json"))["settings"]
VERSION = json.loads(load_fixture("version.json"))
WORKERS = json.loads(load_fixture("workers.json"))

def test_queue() -> None:
    """Test the TaskQueue model."""
    task_queue = models.TaskQueue.from_dict(QUEUE)

    assert task_queue
    assert task_queue.recordsTotal == 654
    assert task_queue.recordsFiltered == 650
    assert len(task_queue.results) == 10

def test_settings() -> None:
    """Test the Settings model."""
    settings = models.Settings.from_dict(SETTINGS)

    assert settings
    assert settings.ui_port == 8888
    assert settings.config_path == "/config/.unmanic/config"
    assert settings.log_path == "/config/.unmanic/logs"
    assert settings.plugins_path == "/config/.unmanic/plugins"
    assert settings.userdata_path == "/config/.unmanic/userdata"
    assert settings.debugging == False
    assert settings.library_path == "/library"
    assert settings.enable_library_scanner == False
    assert settings.schedule_full_scan_minutes == 1440
    assert settings.follow_symlinks == True
    assert settings.concurrent_file_testers == 2 
    assert settings.run_full_scan_on_start == True
    assert settings.enable_inotify == True
    assert settings.clear_pending_tasks_on_restart == True
    assert settings.number_of_workers == 4
    assert settings.cache_path == "/tmp/unmanic"
    assert settings.installation_name == "Unmanic"
    assert settings.distributed_worker_count_target == 0