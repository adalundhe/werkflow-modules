from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_field_index import CloudWatchLogsFieldIndex


class CloudWatchLogsDescribeFieldIndexesResponse(BaseModel):
    fieldIndexes: list[CloudWatchLogsFieldIndex] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
