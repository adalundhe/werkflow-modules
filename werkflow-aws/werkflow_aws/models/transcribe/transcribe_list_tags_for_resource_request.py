from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
