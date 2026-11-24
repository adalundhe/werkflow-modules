from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsUntagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    TagKeys: list[StrictStr]
