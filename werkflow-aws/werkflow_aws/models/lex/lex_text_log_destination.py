from __future__ import annotations
from pydantic import BaseModel
from .lex_cloud_watch_log_group_log_destination import LexCloudWatchLogGroupLogDestination


class LexTextLogDestination(BaseModel):
    cloudWatch: LexCloudWatchLogGroupLogDestination | None = None
