from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
    NextToken: StrictStr | None = None
