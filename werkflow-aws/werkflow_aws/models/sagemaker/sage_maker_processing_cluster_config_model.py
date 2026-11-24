from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_processing_instance_preference_model import SageMakerProcessingInstancePreferenceModel


class SageMakerProcessingClusterConfigModel(BaseModel):
    InstanceCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    InstancePreferences: list[SageMakerProcessingInstancePreferenceModel] | None = None
    SelectedInstanceType: StrictStr | None = None
    SelectedInstanceCount: StrictInt | None = None
