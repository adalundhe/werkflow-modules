from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_substitute_string_entry import CloudWatchLogsSubstituteStringEntry


class CloudWatchLogsSubstituteString(BaseModel):
    entries: list[CloudWatchLogsSubstituteStringEntry] | None = None
