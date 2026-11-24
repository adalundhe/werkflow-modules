from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightKnowledgeBaseScheduleRefreshOnEntity(BaseModel):
    DayOfWeek: StrictStr | None = None
    DayOfMonth: StrictStr | None = None
