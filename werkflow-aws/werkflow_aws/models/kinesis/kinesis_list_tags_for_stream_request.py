from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisListTagsForStreamRequest(BaseModel):
    StreamName: StrictStr | None = None
    ExclusiveStartTagKey: StrictStr | None = None
    Limit: StrictInt | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
