from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_hosted_zone_tier import Route53HostedZoneTier


class Route53HostedZoneConfig(BaseModel):
    Comment: StrictStr | None = None
    PrivateZone: StrictBool | None = None
    HostedZoneTier: Route53HostedZoneTier | None = None
