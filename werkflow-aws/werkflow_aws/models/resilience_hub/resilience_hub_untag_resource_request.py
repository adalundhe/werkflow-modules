from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
