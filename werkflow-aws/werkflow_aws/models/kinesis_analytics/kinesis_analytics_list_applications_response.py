from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_summary import KinesisAnalyticsApplicationSummary


class KinesisAnalyticsListApplicationsResponse(BaseModel):
    ApplicationSummaries: list[KinesisAnalyticsApplicationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
