from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
