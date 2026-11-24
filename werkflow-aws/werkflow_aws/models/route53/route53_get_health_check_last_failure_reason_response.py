from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_health_check_observation_model import Route53HealthCheckObservationModel


class Route53GetHealthCheckLastFailureReasonResponse(BaseModel):
    HealthCheckObservations: list[Route53HealthCheckObservationModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
