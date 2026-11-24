from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_health_check_source_config import Route53HealthCheckSourceConfig


class Route53HealthCheckSource(BaseModel):
    HealthCheckSourceId: StrictStr | None = None
    HealthCheckSourceStatus: StrictStr | None = None
    HealthCheckSourceConfig: Route53HealthCheckSourceConfig | None = None
    StatusReasonCode: StrictStr | None = None
    StatusReason: StrictStr | None = None
