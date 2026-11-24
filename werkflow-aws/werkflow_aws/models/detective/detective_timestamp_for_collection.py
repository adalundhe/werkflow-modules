from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DetectiveTimestampForCollection(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
