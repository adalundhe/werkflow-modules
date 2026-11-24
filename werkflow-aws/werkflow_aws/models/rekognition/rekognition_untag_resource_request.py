from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionUntagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagKeys: list[StrictStr]
