from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_add_on_request import LightsailAddOnRequest
from .lightsail_tag import LightsailTag


class LightsailCreateDiskRequest(BaseModel):
    diskName: StrictStr
    availabilityZone: StrictStr
    sizeInGb: StrictInt
    tags: list[LightsailTag] | None = None
    addOns: list[LightsailAddOnRequest] | None = None
