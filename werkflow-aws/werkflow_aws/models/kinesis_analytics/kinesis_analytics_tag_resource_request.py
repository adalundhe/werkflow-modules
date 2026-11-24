from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_tag import KinesisAnalyticsTag


class KinesisAnalyticsTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[KinesisAnalyticsTag]
