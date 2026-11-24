from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_hosted_zone_type import Route53HostedZoneType


class Route53ListHostedZonesRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    DelegationSetId: StrictStr | None = None
    HostedZoneType: Route53HostedZoneType | None = None
