from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .media_store_metric_policy_rule import MediaStoreMetricPolicyRule


class MediaStoreMetricPolicy(BaseModel):
    ContainerLevelMetrics: StrictStr | None = None
    MetricPolicyRules: list[MediaStoreMetricPolicyRule] | None = None
