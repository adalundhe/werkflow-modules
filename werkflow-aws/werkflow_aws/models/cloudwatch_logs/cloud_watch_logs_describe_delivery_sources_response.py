from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_logs_delivery_source import CloudWatchLogsDeliverySource


class CloudWatchLogsDescribeDeliverySourcesResponse(BaseModel):
    deliverySources: list[CloudWatchLogsDeliverySource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
