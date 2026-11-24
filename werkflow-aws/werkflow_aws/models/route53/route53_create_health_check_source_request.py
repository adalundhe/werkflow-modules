from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_health_check_source_config import Route53HealthCheckSourceConfig
from .route53_tag_model import Route53TagModel


class Route53CreateHealthCheckSourceRequest(BaseModel):
    HealthCheckSourceConfig: Route53HealthCheckSourceConfig
    CallerReference: StrictStr | None = None
    Tags: list[Route53TagModel] | None = None
