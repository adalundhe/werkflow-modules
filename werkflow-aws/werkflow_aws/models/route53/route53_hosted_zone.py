from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_hosted_zone_config import Route53HostedZoneConfig
from .route53_hosted_zone_features import Route53HostedZoneFeatures
from .route53_linked_service import Route53LinkedService


class Route53HostedZone(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    CallerReference: StrictStr | None = None
    Config: Route53HostedZoneConfig | None = None
    ResourceRecordSetCount: StrictInt | None = None
    LinkedService: Route53LinkedService | None = None
    Features: Route53HostedZoneFeatures | None = None
