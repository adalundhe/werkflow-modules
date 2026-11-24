from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_resource_record_set_protection_config import Route53ResourceRecordSetProtectionConfig


class Route53CreateResourceRecordSetProtectionsRequest(BaseModel):
    HostedZoneId: StrictStr
    Protections: list[Route53ResourceRecordSetProtectionConfig]
