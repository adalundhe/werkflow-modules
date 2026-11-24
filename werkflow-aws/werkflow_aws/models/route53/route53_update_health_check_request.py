from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .route53_alarm_identifier_model import Route53AlarmIdentifierModel


class Route53UpdateHealthCheckRequest(BaseModel):
    HealthCheckId: StrictStr
    HealthCheckVersion: StrictInt | None = None
    IPAddress: StrictStr | None = None
    Port: StrictInt | None = None
    ResourcePath: StrictStr | None = None
    FullyQualifiedDomainName: StrictStr | None = None
    SearchString: StrictStr | None = None
    FailureThreshold: StrictInt | None = None
    Inverted: StrictBool | None = None
    Disabled: StrictBool | None = None
    HealthThreshold: StrictInt | None = None
    ChildHealthChecks: list[StrictStr] | None = None
    EnableSNI: StrictBool | None = None
    Regions: list[Literal['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'sa-east-1']] | None = None
    AlarmIdentifier: Route53AlarmIdentifierModel | None = None
    InsufficientDataHealthStatus: Literal['Healthy', 'Unhealthy', 'LastKnownStatus'] | None = None
    ResetElements: list[Literal['FullyQualifiedDomainName', 'Regions', 'ResourcePath', 'ChildHealthChecks']] | None = None
    HealthCheckSourceId: StrictStr | None = None
