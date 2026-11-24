from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerAIBenchmarkNetworkConfig(BaseModel):
    VpcConfig: SageMakerVpcConfigModel | None = None
