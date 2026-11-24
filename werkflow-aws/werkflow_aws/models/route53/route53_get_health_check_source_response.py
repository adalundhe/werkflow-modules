from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_health_check_source import Route53HealthCheckSource


class Route53GetHealthCheckSourceResponse(BaseModel):
    HealthCheckSource: Route53HealthCheckSource | None = None
    ResponseMetadata: dict[str, Any] | None = None
