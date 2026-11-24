from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisUntagResourceRequest(BaseModel):
    TagKeys: list[StrictStr]
    ResourceARN: StrictStr
    StreamId: StrictStr | None = None
