from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_monitoring_subscription import CloudFrontMonitoringSubscription


class CloudFrontCreateMonitoringSubscriptionRequest(BaseModel):
    DistributionId: StrictStr
    MonitoringSubscription: CloudFrontMonitoringSubscription
