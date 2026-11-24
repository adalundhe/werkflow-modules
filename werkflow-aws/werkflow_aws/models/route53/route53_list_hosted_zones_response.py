from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_hosted_zone import Route53HostedZone


class Route53ListHostedZonesResponse(BaseModel):
    HostedZones: list[Route53HostedZone] | None = None
    Marker: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
