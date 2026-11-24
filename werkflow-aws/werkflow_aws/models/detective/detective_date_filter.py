from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DetectiveDateFilter(BaseModel):
    StartInclusive: datetime.datetime | StrictStr
    EndInclusive: datetime.datetime | StrictStr
