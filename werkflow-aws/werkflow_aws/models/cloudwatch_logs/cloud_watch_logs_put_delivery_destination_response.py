from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_watch_logs_delivery_destination import CloudWatchLogsDeliveryDestination


class CloudWatchLogsPutDeliveryDestinationResponse(BaseModel):
    deliveryDestination: CloudWatchLogsDeliveryDestination | None = None
    ResponseMetadata: dict[str, Any] | None = None
