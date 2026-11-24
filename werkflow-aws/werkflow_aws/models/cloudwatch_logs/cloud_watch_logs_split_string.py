from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_split_string_entry import CloudWatchLogsSplitStringEntry


class CloudWatchLogsSplitString(BaseModel):
    entries: list[CloudWatchLogsSplitStringEntry] | None = None
