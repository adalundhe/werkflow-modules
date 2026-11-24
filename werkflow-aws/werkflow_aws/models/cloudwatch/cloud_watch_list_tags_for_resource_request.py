from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
