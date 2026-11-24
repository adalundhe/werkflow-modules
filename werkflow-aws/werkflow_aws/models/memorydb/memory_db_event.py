from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MemoryDBEvent(BaseModel):
    SourceName: StrictStr | None = None
    SourceType: StrictStr | None = None
    Message: StrictStr | None = None
    Date: datetime.datetime | StrictStr | None = None
