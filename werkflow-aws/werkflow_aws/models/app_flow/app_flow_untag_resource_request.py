from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
