from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .sage_maker_vpc_config import SageMakerVpcConfig


class SageMakerNetworkConfig(BaseModel):
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    EnableNetworkIsolation: StrictBool | None = None
    VpcConfig: SageMakerVpcConfig | None = None
