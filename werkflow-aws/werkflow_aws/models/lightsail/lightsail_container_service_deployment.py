from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_container import LightsailContainer
from .lightsail_container_service_endpoint import LightsailContainerServiceEndpoint


class LightsailContainerServiceDeployment(BaseModel):
    version: StrictInt | None = None
    state: StrictStr | None = None
    containers: dict[StrictStr, LightsailContainer] | None = None
    publicEndpoint: LightsailContainerServiceEndpoint | None = None
    createdAt: datetime.datetime | StrictStr | None = None
