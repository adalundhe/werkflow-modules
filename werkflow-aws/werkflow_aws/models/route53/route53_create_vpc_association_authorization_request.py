from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_vpc_model import Route53VPCModel


class Route53CreateVPCAssociationAuthorizationRequest(BaseModel):
    HostedZoneId: StrictStr
    VPC: Route53VPCModel
