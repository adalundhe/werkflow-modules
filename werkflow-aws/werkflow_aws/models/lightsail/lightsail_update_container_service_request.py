from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lightsail_private_registry_access_request import LightsailPrivateRegistryAccessRequest


class LightsailUpdateContainerServiceRequest(BaseModel):
    serviceName: StrictStr
    power: Literal['nano', 'micro', 'small', 'medium', 'large', 'xlarge'] | None = None
    scale: StrictInt | None = None
    isDisabled: StrictBool | None = None
    publicDomainNames: dict[StrictStr, list[StrictStr]] | None = None
    privateRegistryAccess: LightsailPrivateRegistryAccessRequest | None = None
