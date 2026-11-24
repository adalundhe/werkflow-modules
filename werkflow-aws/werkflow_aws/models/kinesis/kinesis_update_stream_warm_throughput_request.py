from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisUpdateStreamWarmThroughputRequest(BaseModel):
    WarmThroughputMiBps: StrictInt
    StreamARN: StrictStr | None = None
    StreamName: StrictStr | None = None
    StreamId: StrictStr | None = None
