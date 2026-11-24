from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_transformed_log_record import CloudWatchLogsTransformedLogRecord


class CloudWatchLogsTestTransformerResponse(BaseModel):
    transformedLogs: list[CloudWatchLogsTransformedLogRecord] | None = None
    ResponseMetadata: dict[str, Any] | None = None
