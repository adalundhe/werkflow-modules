from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
