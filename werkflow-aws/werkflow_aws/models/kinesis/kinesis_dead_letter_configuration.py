from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisDeadLetterConfiguration(BaseModel):
    TargetType: StrictStr | None = None
    MaxReceiveCount: StrictInt | None = None
