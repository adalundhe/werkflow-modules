from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_hosted_zone import Route53HostedZone


class Route53ListHostedZonesByNameResponse(BaseModel):
    HostedZones: list[Route53HostedZone] | None = None
    DNSName: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    NextDNSName: StrictStr | None = None
    NextHostedZoneId: StrictStr | None = None
    MaxItems: StrictStr | None = None
