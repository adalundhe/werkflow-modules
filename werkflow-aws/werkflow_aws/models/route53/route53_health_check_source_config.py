from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_subnet_configuration import Route53SubnetConfiguration


class Route53HealthCheckSourceConfig(BaseModel):
    VpcId: StrictStr | None = None
    SubnetConfigurationList: list[Route53SubnetConfiguration] | None = None
