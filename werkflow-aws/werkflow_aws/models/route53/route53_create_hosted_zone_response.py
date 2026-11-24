from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_change_info import Route53ChangeInfo
from .route53_delegation_set import Route53DelegationSet
from .route53_hosted_zone import Route53HostedZone
from .route53_vpc import Route53VPC


class Route53CreateHostedZoneResponse(BaseModel):
    HostedZone: Route53HostedZone | None = None
    ChangeInfo: Route53ChangeInfo | None = None
    DelegationSet: Route53DelegationSet | None = None
    VPC: Route53VPC | None = None
    Location: StrictStr | None = None
