from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .eks_gateway_api_configuration import EKSGatewayApiConfiguration


class EKSElasticLoadBalancing(BaseModel):
    enabled: StrictBool | None = None
    gatewayApi: EKSGatewayApiConfiguration | None = None
