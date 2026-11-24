from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_knowledge_base_schedule_refresh_on_entity import QuickSightKnowledgeBaseScheduleRefreshOnEntity


class QuickSightKnowledgeBaseRefreshFrequency(BaseModel):
    Interval: StrictStr | None = None
    RefreshOnDay: QuickSightKnowledgeBaseScheduleRefreshOnEntity | None = None
