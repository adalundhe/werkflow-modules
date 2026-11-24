from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
