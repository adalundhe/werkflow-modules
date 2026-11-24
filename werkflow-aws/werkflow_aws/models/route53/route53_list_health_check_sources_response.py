from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_health_check_source import Route53HealthCheckSource


class Route53ListHealthCheckSourcesResponse(BaseModel):
    HealthCheckSources: list[Route53HealthCheckSource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
