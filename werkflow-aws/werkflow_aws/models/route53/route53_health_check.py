from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_cloud_watch_alarm_configuration import Route53CloudWatchAlarmConfiguration
from .route53_health_check_config import Route53HealthCheckConfig
from .route53_linked_service import Route53LinkedService


class Route53HealthCheck(BaseModel):
    Id: StrictStr | None = None
    CallerReference: StrictStr | None = None
    LinkedService: Route53LinkedService | None = None
    HealthCheckConfig: Route53HealthCheckConfig | None = None
    HealthCheckVersion: StrictInt | None = None
    CloudWatchAlarmConfiguration: Route53CloudWatchAlarmConfiguration | None = None
