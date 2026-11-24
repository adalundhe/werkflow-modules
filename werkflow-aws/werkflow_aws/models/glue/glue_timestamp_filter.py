from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueTimestampFilter(BaseModel):
    RecordedBefore: datetime.datetime | StrictStr | None = None
    RecordedAfter: datetime.datetime | StrictStr | None = None
