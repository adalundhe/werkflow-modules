from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_health_check_region import Route53HealthCheckRegion
from .route53_status_report import Route53StatusReport


class Route53HealthCheckObservation(BaseModel):
    Region: Route53HealthCheckRegion | None = None
    IPAddress: StrictStr | None = None
    StatusReport: Route53StatusReport | None = None
