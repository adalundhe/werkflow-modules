from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_rename_key_entry import CloudWatchLogsRenameKeyEntry


class CloudWatchLogsRenameKeys(BaseModel):
    entries: list[CloudWatchLogsRenameKeyEntry] | None = None
