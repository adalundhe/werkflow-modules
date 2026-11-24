from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_health_check_model import Route53HealthCheckModel


class Route53ListHealthChecksBySourceResponse(BaseModel):
    HealthChecks: list[Route53HealthCheckModel] | None = None
    Marker: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
