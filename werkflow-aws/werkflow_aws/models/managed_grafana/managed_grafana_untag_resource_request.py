from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
