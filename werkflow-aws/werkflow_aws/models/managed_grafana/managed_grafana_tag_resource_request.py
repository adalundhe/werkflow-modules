from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
