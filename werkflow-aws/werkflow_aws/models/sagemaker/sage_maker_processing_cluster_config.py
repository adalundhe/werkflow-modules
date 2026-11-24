from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_processing_instance_preference import SageMakerProcessingInstancePreference
from .sage_maker_processing_instance_type import SageMakerProcessingInstanceType


class SageMakerProcessingClusterConfig(BaseModel):
    InstanceCount: StrictInt | None = None
    InstanceType: SageMakerProcessingInstanceType | None = None
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    InstancePreferences: list[SageMakerProcessingInstancePreference] | None = None
    SelectedInstanceType: SageMakerProcessingInstanceType | None = None
    SelectedInstanceCount: StrictInt | None = None
