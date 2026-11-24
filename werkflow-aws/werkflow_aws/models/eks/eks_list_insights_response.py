from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .eks_insight_summary import EKSInsightSummary


class EKSListInsightsResponse(BaseModel):
    insights: list[EKSInsightSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
