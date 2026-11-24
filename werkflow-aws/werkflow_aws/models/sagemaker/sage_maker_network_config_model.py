from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerNetworkConfigModel(BaseModel):
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    EnableNetworkIsolation: StrictBool | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
