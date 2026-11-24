from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_container_service_deployment_request import LightsailContainerServiceDeploymentRequest
from .lightsail_private_registry_access_request import LightsailPrivateRegistryAccessRequest
from .lightsail_tag import LightsailTag


class LightsailCreateContainerServiceRequest(BaseModel):
    serviceName: StrictStr
    power: Literal['nano', 'micro', 'small', 'medium', 'large', 'xlarge']
    scale: StrictInt
    tags: list[LightsailTag] | None = None
    publicDomainNames: dict[StrictStr, list[StrictStr]] | None = None
    deployment: LightsailContainerServiceDeploymentRequest | None = None
    privateRegistryAccess: LightsailPrivateRegistryAccessRequest | None = None
