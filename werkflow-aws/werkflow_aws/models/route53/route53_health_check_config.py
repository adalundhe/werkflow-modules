from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_alarm_identifier import Route53AlarmIdentifier
from .route53_endpoint_type import Route53EndpointType
from .route53_health_check_region import Route53HealthCheckRegion
from .route53_health_check_type import Route53HealthCheckType
from .route53_insufficient_data_health_status import Route53InsufficientDataHealthStatus


class Route53HealthCheckConfig(BaseModel):
    IPAddress: StrictStr | None = None
    Port: StrictInt | None = None
    Type: Route53HealthCheckType | None = None
    ResourcePath: StrictStr | None = None
    FullyQualifiedDomainName: StrictStr | None = None
    SearchString: StrictStr | None = None
    RequestInterval: StrictInt | None = None
    FailureThreshold: StrictInt | None = None
    MeasureLatency: StrictBool | None = None
    Inverted: StrictBool | None = None
    Disabled: StrictBool | None = None
    HealthThreshold: StrictInt | None = None
    ChildHealthChecks: list[StrictStr] | None = None
    EnableSNI: StrictBool | None = None
    Regions: list[Route53HealthCheckRegion] | None = None
    AlarmIdentifier: Route53AlarmIdentifier | None = None
    InsufficientDataHealthStatus: Route53InsufficientDataHealthStatus | None = None
    RoutingControlArn: StrictStr | None = None
    EndpointType: Route53EndpointType | None = None
    HealthCheckSourceId: StrictStr | None = None
