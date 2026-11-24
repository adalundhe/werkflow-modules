from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_vpc_config_model import SageMakerVpcConfigModel


class SageMakerLabelingJobResourceConfig(BaseModel):
    VolumeKmsKeyId: StrictStr | None = None
    VpcConfig: SageMakerVpcConfigModel | None = None
