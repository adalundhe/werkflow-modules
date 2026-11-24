from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: dict[StrictStr, StrictStr]
