from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
