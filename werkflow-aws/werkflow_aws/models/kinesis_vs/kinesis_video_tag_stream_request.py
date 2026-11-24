from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoTagStreamRequest(BaseModel):
    Tags: dict[StrictStr, StrictStr]
    StreamARN: StrictStr | None = None
    StreamName: StrictStr | None = None
