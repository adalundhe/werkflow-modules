from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .eks_gateway_api_configuration_model import EKSGatewayApiConfigurationModel


class EKSElasticLoadBalancingModel(BaseModel):
    enabled: StrictBool | None = None
    gatewayApi: EKSGatewayApiConfigurationModel | None = None
