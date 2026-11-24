from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_container_service_registry_login import LightsailContainerServiceRegistryLogin


class LightsailCreateContainerServiceRegistryLoginResponse(BaseModel):
    registryLogin: LightsailContainerServiceRegistryLogin | None = None
    ResponseMetadata: dict[str, Any] | None = None
