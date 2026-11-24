from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontRealtimeMetricsSubscriptionConfig(BaseModel):
    RealtimeMetricsSubscriptionStatus: StrictStr | None = None
