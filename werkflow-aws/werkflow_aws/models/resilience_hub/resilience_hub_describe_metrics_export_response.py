from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .resilience_hub_s3_location import ResilienceHubS3Location


class ResilienceHubDescribeMetricsExportResponse(BaseModel):
    errorMessage: StrictStr | None = None
    exportLocation: ResilienceHubS3Location | None = None
    metricsExportId: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
