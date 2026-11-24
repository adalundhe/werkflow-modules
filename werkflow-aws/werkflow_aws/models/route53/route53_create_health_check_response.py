from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_health_check import Route53HealthCheck


class Route53CreateHealthCheckResponse(BaseModel):
    HealthCheck: Route53HealthCheck | None = None
    Location: StrictStr | None = None
