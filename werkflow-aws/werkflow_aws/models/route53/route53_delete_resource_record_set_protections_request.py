from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_resource_record_set_protection_key import Route53ResourceRecordSetProtectionKey


class Route53DeleteResourceRecordSetProtectionsRequest(BaseModel):
    HostedZoneId: StrictStr
    Protections: list[Route53ResourceRecordSetProtectionKey]
