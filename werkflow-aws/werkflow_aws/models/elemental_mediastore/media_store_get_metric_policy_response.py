from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .media_store_metric_policy import MediaStoreMetricPolicy


class MediaStoreGetMetricPolicyResponse(BaseModel):
    MetricPolicy: MediaStoreMetricPolicy | None = None
    ResponseMetadata: dict[str, Any] | None = None
