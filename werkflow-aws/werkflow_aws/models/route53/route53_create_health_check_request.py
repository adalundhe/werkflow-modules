from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_health_check_config import Route53HealthCheckConfig


class Route53CreateHealthCheckRequest(BaseModel):
    CallerReference: StrictStr
    HealthCheckConfig: Route53HealthCheckConfig
