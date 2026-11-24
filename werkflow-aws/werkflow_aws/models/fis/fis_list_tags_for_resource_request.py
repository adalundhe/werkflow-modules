from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
