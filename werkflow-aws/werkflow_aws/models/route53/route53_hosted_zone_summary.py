from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_hosted_zone_owner import Route53HostedZoneOwner


class Route53HostedZoneSummary(BaseModel):
    HostedZoneId: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: Route53HostedZoneOwner | None = None
