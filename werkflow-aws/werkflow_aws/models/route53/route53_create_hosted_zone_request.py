from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_change_guardrail import Route53ChangeGuardrail
from .route53_hosted_zone_config import Route53HostedZoneConfig
from .route53_vpc import Route53VPC


class Route53CreateHostedZoneRequest(BaseModel):
    Name: StrictStr
    CallerReference: StrictStr
    VPC: Route53VPC | None = None
    HostedZoneConfig: Route53HostedZoneConfig | None = None
    DelegationSetId: StrictStr | None = None
    EnablePublicDNSFallback: StrictBool | None = None
    ChangeGuardrails: list[Route53ChangeGuardrail] | None = None
