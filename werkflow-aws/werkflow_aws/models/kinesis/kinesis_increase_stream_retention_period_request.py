from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisIncreaseStreamRetentionPeriodRequest(BaseModel):
    RetentionPeriodHours: StrictInt
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
