from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_vpc_model import Route53VPCModel


class Route53CreateVPCAssociationAuthorizationResponse(BaseModel):
    HostedZoneId: StrictStr | None = None
    VPC: Route53VPCModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
