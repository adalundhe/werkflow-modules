from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisQueueStreamFilter(BaseModel):
    StreamARN: StrictStr
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
