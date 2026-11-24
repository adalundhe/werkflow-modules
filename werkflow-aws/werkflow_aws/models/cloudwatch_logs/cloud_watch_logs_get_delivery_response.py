from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_delivery import CloudWatchLogsDelivery


class CloudWatchLogsGetDeliveryResponse(BaseModel):
    delivery: CloudWatchLogsDelivery | None = None
    ResponseMetadata: dict[str, Any] | None = None
