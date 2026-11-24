from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .route53_hosted_zone_limit import Route53HostedZoneLimit


class Route53GetHostedZoneLimitResponse(BaseModel):
    Limit: Route53HostedZoneLimit | None = None
    Count: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
