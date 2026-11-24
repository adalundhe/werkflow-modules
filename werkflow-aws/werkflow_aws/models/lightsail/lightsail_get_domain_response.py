from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_domain import LightsailDomain


class LightsailGetDomainResponse(BaseModel):
    domain: LightsailDomain | None = None
    ResponseMetadata: dict[str, Any] | None = None
