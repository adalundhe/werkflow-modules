from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
