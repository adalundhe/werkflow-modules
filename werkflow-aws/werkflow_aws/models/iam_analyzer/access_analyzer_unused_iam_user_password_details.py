from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AccessAnalyzerUnusedIamUserPasswordDetails(BaseModel):
    lastAccessed: datetime.datetime | StrictStr | None = None
