from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMAccessKeyLastUsed(BaseModel):
    LastUsedDate: datetime.datetime | StrictStr | None = None
    ServiceName: StrictStr | None = None
    Region: StrictStr | None = None
