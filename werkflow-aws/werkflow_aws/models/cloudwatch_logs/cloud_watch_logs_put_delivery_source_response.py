from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_delivery_source import CloudWatchLogsDeliverySource


class CloudWatchLogsPutDeliverySourceResponse(BaseModel):
    deliverySource: CloudWatchLogsDeliverySource | None = None
    ResponseMetadata: dict[str, Any] | None = None
