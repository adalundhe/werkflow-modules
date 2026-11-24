from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ACMTimestampRange(BaseModel):
    Start: datetime.datetime | StrictStr | None = None
    End: datetime.datetime | StrictStr | None = None
