from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BackupDateRange(BaseModel):
    FromDate: datetime.datetime | StrictStr | None = None
    ToDate: datetime.datetime | StrictStr | None = None
