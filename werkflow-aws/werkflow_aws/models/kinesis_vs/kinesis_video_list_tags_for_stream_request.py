from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoListTagsForStreamRequest(BaseModel):
    NextToken: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamName: StrictStr | None = None
