from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WAFv2VisibilityConfig(BaseModel):
    SampledRequestsEnabled: StrictBool | None = None
    CloudWatchMetricsEnabled: StrictBool | None = None
    MetricName: StrictStr | None = None
