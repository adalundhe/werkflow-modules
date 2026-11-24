from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_cloud_watch_alarm_configuration_model import Route53CloudWatchAlarmConfigurationModel
from .route53_health_check_config_model import Route53HealthCheckConfigModel
from .route53_linked_service_model import Route53LinkedServiceModel


class Route53HealthCheckModel(BaseModel):
    Id: StrictStr | None = None
    CallerReference: StrictStr | None = None
    LinkedService: Route53LinkedServiceModel | None = None
    HealthCheckConfig: Route53HealthCheckConfigModel | None = None
    HealthCheckVersion: StrictInt | None = None
    CloudWatchAlarmConfiguration: Route53CloudWatchAlarmConfigurationModel | None = None
