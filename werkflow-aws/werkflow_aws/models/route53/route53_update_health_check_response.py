from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_health_check_model import Route53HealthCheckModel


class Route53UpdateHealthCheckResponse(BaseModel):
    HealthCheck: Route53HealthCheckModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
