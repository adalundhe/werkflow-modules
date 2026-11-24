from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AthenaNotebookSessionSummary(BaseModel):
    SessionId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
