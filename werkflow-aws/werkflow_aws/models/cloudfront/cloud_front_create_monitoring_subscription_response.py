from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_monitoring_subscription import CloudFrontMonitoringSubscription


class CloudFrontCreateMonitoringSubscriptionResponse(BaseModel):
    MonitoringSubscription: CloudFrontMonitoringSubscription | None = None
    ResponseMetadata: dict[str, Any] | None = None
