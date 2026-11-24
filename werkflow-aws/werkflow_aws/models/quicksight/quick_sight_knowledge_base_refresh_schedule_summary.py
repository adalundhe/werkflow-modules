from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_knowledge_base_refresh_frequency import QuickSightKnowledgeBaseRefreshFrequency


class QuickSightKnowledgeBaseRefreshScheduleSummary(BaseModel):
    ScheduleId: StrictStr | None = None
    ScheduleFrequency: QuickSightKnowledgeBaseRefreshFrequency | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
