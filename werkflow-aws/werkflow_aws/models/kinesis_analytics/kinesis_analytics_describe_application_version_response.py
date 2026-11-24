from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_analytics_application_detail import KinesisAnalyticsApplicationDetail


class KinesisAnalyticsDescribeApplicationVersionResponse(BaseModel):
    ApplicationVersionDetail: KinesisAnalyticsApplicationDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
