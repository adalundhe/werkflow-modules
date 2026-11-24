from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisQueueStartingPosition(BaseModel):
    Type: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
