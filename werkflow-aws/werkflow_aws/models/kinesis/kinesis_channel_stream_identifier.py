from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisChannelStreamIdentifier(BaseModel):
    StreamARN: StrictStr | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
