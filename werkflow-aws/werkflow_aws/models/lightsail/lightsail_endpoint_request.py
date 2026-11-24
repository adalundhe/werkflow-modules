from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_container_service_health_check_config import LightsailContainerServiceHealthCheckConfig


class LightsailEndpointRequest(BaseModel):
    containerName: StrictStr
    containerPort: StrictInt
    healthCheck: LightsailContainerServiceHealthCheckConfig | None = None
