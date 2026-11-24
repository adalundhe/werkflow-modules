from __future__ import annotations
from pydantic import BaseModel
from .route53_health_check import Route53HealthCheck


class Route53GetHealthCheckResponse(BaseModel):
    HealthCheck: Route53HealthCheck | None = None
