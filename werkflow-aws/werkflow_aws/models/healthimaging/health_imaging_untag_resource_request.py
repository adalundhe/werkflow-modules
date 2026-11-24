from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
