from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailTagResourceRequest(BaseModel):
    resourceName: StrictStr
    tags: list[LightsailTag]
    resourceArn: StrictStr | None = None
