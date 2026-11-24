from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
