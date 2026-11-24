from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoUntagStreamRequest(BaseModel):
    TagKeyList: list[StrictStr]
    StreamARN: StrictStr | None = None
    StreamName: StrictStr | None = None
