from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_add_key_entry import CloudWatchLogsAddKeyEntry


class CloudWatchLogsAddKeys(BaseModel):
    entries: list[CloudWatchLogsAddKeyEntry] | None = None
