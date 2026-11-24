from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_get_log_object_response_stream import CloudWatchLogsGetLogObjectResponseStream


class CloudWatchLogsGetLogObjectResponse(BaseModel):
    fieldStream: CloudWatchLogsGetLogObjectResponseStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
