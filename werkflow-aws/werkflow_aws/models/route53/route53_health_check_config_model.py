from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_alarm_identifier_model import Route53AlarmIdentifierModel


class Route53HealthCheckConfigModel(BaseModel):
    IPAddress: StrictStr | None = None
    Port: StrictInt | None = None
    Type: StrictStr | None = None
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
    Regions: list[StrictStr] | None = None
    AlarmIdentifier: Route53AlarmIdentifierModel | None = None
    InsufficientDataHealthStatus: StrictStr | None = None
    RoutingControlArn: StrictStr | None = None
    EndpointType: StrictStr | None = None
    HealthCheckSourceId: StrictStr | None = None
