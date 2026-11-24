from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_knowledge_base_summary import QuickSightKnowledgeBaseSummary


class QuickSightSearchKnowledgeBasesResponse(BaseModel):
    KnowledgeBaseSummaries: list[QuickSightKnowledgeBaseSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
