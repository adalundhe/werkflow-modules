from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_copy_value_entry import CloudWatchLogsCopyValueEntry


class CloudWatchLogsCopyValue(BaseModel):
    entries: list[CloudWatchLogsCopyValueEntry] | None = None
