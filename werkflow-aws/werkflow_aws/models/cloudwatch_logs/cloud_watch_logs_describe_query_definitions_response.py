from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_query_definition import CloudWatchLogsQueryDefinition


class CloudWatchLogsDescribeQueryDefinitionsResponse(BaseModel):
    queryDefinitions: list[CloudWatchLogsQueryDefinition] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
