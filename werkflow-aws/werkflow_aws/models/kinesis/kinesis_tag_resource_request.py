from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisTagResourceRequest(BaseModel):
    Tags: dict[StrictStr, StrictStr]
    ResourceARN: StrictStr
    StreamId: StrictStr | None = None
