from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_hyper_parameter_tuning_instance_config import SageMakerHyperParameterTuningInstanceConfig


class SageMakerHyperParameterTuningResourceConfig(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    AllocationStrategy: StrictStr | None = None
    InstanceConfigs: list[SageMakerHyperParameterTuningInstanceConfig] | None = None
