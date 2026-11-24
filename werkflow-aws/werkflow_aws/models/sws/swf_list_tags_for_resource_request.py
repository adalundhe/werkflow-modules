from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
