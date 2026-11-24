from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsWafv2VisibilityConfigDetails(BaseModel):
    CloudWatchMetricsEnabled: StrictBool | None = None
    MetricName: StrictStr | None = None
    SampledRequestsEnabled: StrictBool | None = None
