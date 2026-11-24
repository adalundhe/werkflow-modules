from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_container import LightsailContainer
from .lightsail_endpoint_request import LightsailEndpointRequest


class LightsailCreateContainerServiceDeploymentRequest(BaseModel):
    serviceName: StrictStr
    containers: dict[StrictStr, LightsailContainer] | None = None
    publicEndpoint: LightsailEndpointRequest | None = None
