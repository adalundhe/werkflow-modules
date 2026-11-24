from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_health_check import Route53HealthCheck


class Route53ListHealthChecksResponse(BaseModel):
    HealthChecks: list[Route53HealthCheck] | None = None
    Marker: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
