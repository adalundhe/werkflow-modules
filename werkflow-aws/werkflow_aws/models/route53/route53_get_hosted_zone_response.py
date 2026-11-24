from __future__ import annotations
from pydantic import BaseModel
from .route53_delegation_set import Route53DelegationSet
from .route53_hosted_zone import Route53HostedZone
from .route53_vpc import Route53VPC


class Route53GetHostedZoneResponse(BaseModel):
    HostedZone: Route53HostedZone | None = None
    DelegationSet: Route53DelegationSet | None = None
    VPCs: list[Route53VPC] | None = None
