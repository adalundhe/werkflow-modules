from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_destination import CloudWatchLogsDestination


class CloudWatchLogsDescribeDestinationsResponse(BaseModel):
    destinations: list[CloudWatchLogsDestination] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
