from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisStreamFilter(BaseModel):
    StreamARN: StrictStr
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
