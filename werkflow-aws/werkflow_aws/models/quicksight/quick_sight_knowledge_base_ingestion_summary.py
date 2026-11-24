from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightKnowledgeBaseIngestionSummary(BaseModel):
    IngestionId: StrictStr | None = None
    IngestionStatus: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
