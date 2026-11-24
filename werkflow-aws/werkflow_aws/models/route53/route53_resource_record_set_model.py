from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_az_affinity_model import Route53AZAffinityModel
from .route53_alias_target_model import Route53AliasTargetModel
from .route53_cidr_routing_config_model import Route53CidrRoutingConfigModel
from .route53_geo_location_model import Route53GeoLocationModel
from .route53_geo_proximity_location_model import Route53GeoProximityLocationModel
from .route53_resource_record_model import Route53ResourceRecordModel


class Route53ResourceRecordSetModel(BaseModel):
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    SetIdentifier: StrictStr | None = None
    Weight: StrictInt | None = None
    Region: StrictStr | None = None
    GeoLocation: Route53GeoLocationModel | None = None
    Failover: StrictStr | None = None
    MultiValueAnswer: StrictBool | None = None
    TTL: StrictInt | None = None
    ResourceRecords: list[Route53ResourceRecordModel] | None = None
    AliasTarget: Route53AliasTargetModel | None = None
    HealthCheckId: StrictStr | None = None
    TrafficPolicyInstanceId: StrictStr | None = None
    CidrRoutingConfig: Route53CidrRoutingConfigModel | None = None
    GeoProximityLocation: Route53GeoProximityLocationModel | None = None
    AZAffinity: Route53AZAffinityModel | None = None
