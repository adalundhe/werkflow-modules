from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dev_ops_guru_proactive_organization_insight_summary import DevOpsGuruProactiveOrganizationInsightSummary
from .dev_ops_guru_reactive_organization_insight_summary import DevOpsGuruReactiveOrganizationInsightSummary


class DevOpsGuruListOrganizationInsightsResponse(BaseModel):
    ProactiveInsights: list[DevOpsGuruProactiveOrganizationInsightSummary] | None = None
    ReactiveInsights: list[DevOpsGuruReactiveOrganizationInsightSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
