from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisVideoLastRecorderStatus(BaseModel):
    JobStatusDetails: StrictStr | None = None
    LastCollectedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    RecorderStatus: StrictStr | None = None
