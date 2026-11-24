from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_knowledge_base_refresh_schedule_summary import QuickSightKnowledgeBaseRefreshScheduleSummary


class QuickSightListKnowledgeBaseRefreshSchedulesResponse(BaseModel):
    ScheduleSummaries: list[QuickSightKnowledgeBaseRefreshScheduleSummary] | None = None
    KnowledgeBaseArn: StrictStr | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
