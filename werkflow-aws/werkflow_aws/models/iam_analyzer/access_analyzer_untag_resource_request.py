from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
