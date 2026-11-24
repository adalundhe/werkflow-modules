from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeMetricsExportRequest(BaseModel):
    metricsExportId: StrictStr
