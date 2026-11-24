from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisVideoScheduleConfig(BaseModel):
    ScheduleExpression: StrictStr | None = None
    DurationInSeconds: StrictInt | None = None
