from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerAutoMLSecurityConfig(BaseModel):
    VolumeKmsKeyId: StrictStr | None = None
    EnableInterContainerTrafficEncryption: StrictBool | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
