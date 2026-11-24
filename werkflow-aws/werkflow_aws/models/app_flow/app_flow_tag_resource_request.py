from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
