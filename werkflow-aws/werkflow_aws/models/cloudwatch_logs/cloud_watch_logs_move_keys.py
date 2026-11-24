from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_logs_move_key_entry import CloudWatchLogsMoveKeyEntry


class CloudWatchLogsMoveKeys(BaseModel):
    entries: list[CloudWatchLogsMoveKeyEntry] | None = None
