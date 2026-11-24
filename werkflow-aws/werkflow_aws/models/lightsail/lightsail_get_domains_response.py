from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_domain import LightsailDomain


class LightsailGetDomainsResponse(BaseModel):
    domains: list[LightsailDomain] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
