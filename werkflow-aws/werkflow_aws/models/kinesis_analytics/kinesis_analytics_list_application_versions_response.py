from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_version_summary import KinesisAnalyticsApplicationVersionSummary


class KinesisAnalyticsListApplicationVersionsResponse(BaseModel):
    ApplicationVersionSummaries: list[KinesisAnalyticsApplicationVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
