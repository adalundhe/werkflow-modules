from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMRoleLastUsedModel(BaseModel):
    LastUsedDate: datetime.datetime | StrictStr | None = None
    Region: StrictStr | None = None
