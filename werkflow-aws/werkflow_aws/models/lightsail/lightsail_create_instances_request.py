from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .lightsail_add_on_request import LightsailAddOnRequest
from .lightsail_tag import LightsailTag


class LightsailCreateInstancesRequest(BaseModel):
    instanceNames: list[StrictStr]
    availabilityZone: StrictStr
    blueprintId: StrictStr
    bundleId: StrictStr
    customImageName: StrictStr | None = None
    userData: StrictStr | None = None
    keyPairName: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    addOns: list[LightsailAddOnRequest] | None = None
    ipAddressType: Literal['dualstack', 'ipv4', 'ipv6'] | None = None
