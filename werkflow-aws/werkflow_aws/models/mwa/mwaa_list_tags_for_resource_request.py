from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MWAAListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
