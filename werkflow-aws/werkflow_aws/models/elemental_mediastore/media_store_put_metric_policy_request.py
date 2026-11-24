from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .media_store_metric_policy import MediaStoreMetricPolicy


class MediaStorePutMetricPolicyRequest(BaseModel):
    ContainerName: StrictStr
    MetricPolicy: MediaStoreMetricPolicy
