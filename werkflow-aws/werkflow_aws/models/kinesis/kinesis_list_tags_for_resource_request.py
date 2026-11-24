from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
    StreamId: StrictStr | None = None
