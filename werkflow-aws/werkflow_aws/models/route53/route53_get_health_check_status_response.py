from __future__ import annotations
from pydantic import BaseModel
from .route53_health_check_observation import Route53HealthCheckObservation


class Route53GetHealthCheckStatusResponse(BaseModel):
    HealthCheckObservations: list[Route53HealthCheckObservation] | None = None
