from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateKeyPairRequest(BaseModel):
    keyPairName: StrictStr
    tags: list[LightsailTag] | None = None
