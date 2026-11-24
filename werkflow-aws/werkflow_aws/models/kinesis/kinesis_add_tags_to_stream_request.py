from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAddTagsToStreamRequest(BaseModel):
    Tags: dict[StrictStr, StrictStr]
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
