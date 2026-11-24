from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailUntagResourceRequest(BaseModel):
    resourceName: StrictStr
    tagKeys: list[StrictStr]
    resourceArn: StrictStr | None = None
