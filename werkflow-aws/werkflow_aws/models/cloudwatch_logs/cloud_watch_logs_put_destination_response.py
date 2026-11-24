from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_destination import CloudWatchLogsDestination


class CloudWatchLogsPutDestinationResponse(BaseModel):
    destination: CloudWatchLogsDestination | None = None
    ResponseMetadata: dict[str, Any] | None = None
