from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateDomainRequest(BaseModel):
    domainName: StrictStr
    tags: list[LightsailTag] | None = None
