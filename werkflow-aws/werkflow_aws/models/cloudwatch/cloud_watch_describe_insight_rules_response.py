from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_watch_insight_rule import CloudWatchInsightRule


class CloudWatchDescribeInsightRulesResponse(BaseModel):
    NextToken: StrictStr | None = None
    InsightRules: list[CloudWatchInsightRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
