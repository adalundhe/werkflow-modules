from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_knowledge_base_refresh_frequency import QuickSightKnowledgeBaseRefreshFrequency


class QuickSightUpdateKnowledgeBaseRefreshScheduleRequest(BaseModel):
    AwsAccountId: StrictStr
    KnowledgeBaseId: StrictStr
    ScheduleId: StrictStr
    ScheduleFrequency: QuickSightKnowledgeBaseRefreshFrequency | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    State: Literal['ENABLED', 'DISABLED'] | None = None
