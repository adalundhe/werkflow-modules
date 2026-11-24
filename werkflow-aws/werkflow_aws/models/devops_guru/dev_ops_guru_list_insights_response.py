from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_proactive_insight_summary import DevOpsGuruProactiveInsightSummary
from .dev_ops_guru_reactive_insight_summary import DevOpsGuruReactiveInsightSummary


class DevOpsGuruListInsightsResponse(BaseModel):
    ProactiveInsights: list[DevOpsGuruProactiveInsightSummary] | None = None
    ReactiveInsights: list[DevOpsGuruReactiveInsightSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
