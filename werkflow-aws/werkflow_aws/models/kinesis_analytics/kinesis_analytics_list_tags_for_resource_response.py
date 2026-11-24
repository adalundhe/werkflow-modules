from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_analytics_tag import KinesisAnalyticsTag


class KinesisAnalyticsListTagsForResourceResponse(BaseModel):
    Tags: list[KinesisAnalyticsTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
