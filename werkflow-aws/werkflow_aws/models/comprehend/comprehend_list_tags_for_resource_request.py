from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
