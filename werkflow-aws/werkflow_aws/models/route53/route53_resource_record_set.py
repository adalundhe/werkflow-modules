from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_alias_target import Route53AliasTarget
from .route53_az_affinity import Route53AZAffinity
from .route53_cidr_routing_config import Route53CidrRoutingConfig
from .route53_geo_location import Route53GeoLocation
from .route53_geo_proximity_location import Route53GeoProximityLocation
from .route53_resource_record import Route53ResourceRecord
from .route53_resource_record_set_failover import Route53ResourceRecordSetFailover
from .route53_resource_record_set_region import Route53ResourceRecordSetRegion
from .route53_rr_type import Route53RRType


class Route53ResourceRecordSet(BaseModel):
    Name: StrictStr | None = None
    Type: Route53RRType | None = None
    SetIdentifier: StrictStr | None = None
    Weight: StrictInt | None = None
    Region: Route53ResourceRecordSetRegion | None = None
    GeoLocation: Route53GeoLocation | None = None
    Failover: Route53ResourceRecordSetFailover | None = None
    MultiValueAnswer: StrictBool | None = None
    TTL: StrictInt | None = None
    ResourceRecords: list[Route53ResourceRecord] | None = None
    AliasTarget: Route53AliasTarget | None = None
    HealthCheckId: StrictStr | None = None
    TrafficPolicyInstanceId: StrictStr | None = None
    CidrRoutingConfig: Route53CidrRoutingConfig | None = None
    GeoProximityLocation: Route53GeoProximityLocation | None = None
    AZAffinity: Route53AZAffinity | None = None
