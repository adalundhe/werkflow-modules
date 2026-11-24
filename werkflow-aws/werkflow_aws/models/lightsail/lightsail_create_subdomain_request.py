from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateSubdomainRequest(BaseModel):
    subdomainName: StrictStr
    tags: list[LightsailTag] | None = None
