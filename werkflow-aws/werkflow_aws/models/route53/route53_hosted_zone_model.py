from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_hosted_zone_config_model import Route53HostedZoneConfigModel
from .route53_hosted_zone_features_model import Route53HostedZoneFeaturesModel
from .route53_linked_service_model import Route53LinkedServiceModel


class Route53HostedZoneModel(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    CallerReference: StrictStr | None = None
    Config: Route53HostedZoneConfigModel | None = None
    ResourceRecordSetCount: StrictInt | None = None
    LinkedService: Route53LinkedServiceModel | None = None
    Features: Route53HostedZoneFeaturesModel | None = None
