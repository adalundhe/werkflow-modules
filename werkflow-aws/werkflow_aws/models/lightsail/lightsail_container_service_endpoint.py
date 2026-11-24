from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_container_service_health_check_config import LightsailContainerServiceHealthCheckConfig


class LightsailContainerServiceEndpoint(BaseModel):
    containerName: StrictStr | None = None
    containerPort: StrictInt | None = None
    healthCheck: LightsailContainerServiceHealthCheckConfig | None = None
