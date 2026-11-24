from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_operation import LightsailOperation
from .lightsail_subdomain import LightsailSubdomain


class LightsailCreateSubdomainResponse(BaseModel):
    subdomain: LightsailSubdomain | None = None
    operation: LightsailOperation | None = None
    ResponseMetadata: dict[str, Any] | None = None
