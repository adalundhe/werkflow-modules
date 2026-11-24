from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateContactMethodRequest(BaseModel):
    protocol: Literal['Email', 'SMS']
    contactEndpoint: StrictStr
    tags: list[LightsailTag] | None = None
