from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AccessAnalyzerUnusedAction(BaseModel):
    action: StrictStr | None = None
    lastAccessed: datetime.datetime | StrictStr | None = None
