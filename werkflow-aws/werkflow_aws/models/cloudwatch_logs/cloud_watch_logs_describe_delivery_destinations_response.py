from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_delivery_destination import CloudWatchLogsDeliveryDestination


class CloudWatchLogsDescribeDeliveryDestinationsResponse(BaseModel):
    deliveryDestinations: list[CloudWatchLogsDeliveryDestination] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
