from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EnableAwsNetworkPerformanceMetricSubscriptionRequest(BaseModel):
    Source: StrictStr | None = None
    Destination: StrictStr | None = None
    Metric: Literal['aggregate-latency'] | None = None
    Statistic: Literal['p50'] | None = None
    DryRun: StrictBool | None = None
