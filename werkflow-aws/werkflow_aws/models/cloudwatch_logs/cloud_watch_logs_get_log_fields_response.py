from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_log_fields_list_item import CloudWatchLogsLogFieldsListItem


class CloudWatchLogsGetLogFieldsResponse(BaseModel):
    logFields: list[CloudWatchLogsLogFieldsListItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
