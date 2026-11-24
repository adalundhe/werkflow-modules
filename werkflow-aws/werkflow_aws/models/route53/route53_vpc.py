from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_vpc_region import Route53VPCRegion


class Route53VPC(BaseModel):
    VPCRegion: Route53VPCRegion | None = None
    VPCId: StrictStr | None = None
