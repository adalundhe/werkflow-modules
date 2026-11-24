from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_subdomain import LightsailSubdomain


class LightsailGetSubdomainsResponse(BaseModel):
    subdomains: list[LightsailSubdomain] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
