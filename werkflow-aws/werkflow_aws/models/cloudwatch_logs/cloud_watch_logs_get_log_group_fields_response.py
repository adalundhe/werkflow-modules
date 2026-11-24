from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_log_group_field import CloudWatchLogsLogGroupField


class CloudWatchLogsGetLogGroupFieldsResponse(BaseModel):
    logGroupFields: list[CloudWatchLogsLogGroupField] | None = None
    ResponseMetadata: dict[str, Any] | None = None
