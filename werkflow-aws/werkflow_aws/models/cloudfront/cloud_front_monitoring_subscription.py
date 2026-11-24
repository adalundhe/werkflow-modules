from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_realtime_metrics_subscription_config import CloudFrontRealtimeMetricsSubscriptionConfig


class CloudFrontMonitoringSubscription(BaseModel):
    RealtimeMetricsSubscriptionConfig: CloudFrontRealtimeMetricsSubscriptionConfig | None = None
