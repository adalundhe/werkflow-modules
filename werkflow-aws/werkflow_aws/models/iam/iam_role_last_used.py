from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMRoleLastUsed(BaseModel):
    LastUsedDate: datetime.datetime | None = None
    Region: StrictStr | None = None
