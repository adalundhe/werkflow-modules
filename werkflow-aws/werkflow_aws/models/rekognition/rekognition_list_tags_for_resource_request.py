from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
