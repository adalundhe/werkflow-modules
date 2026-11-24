from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DetectiveTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: dict[StrictStr, StrictStr]
