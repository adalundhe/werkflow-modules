from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruRecommendationRelatedCloudWatchMetricsSourceDetail(BaseModel):
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
