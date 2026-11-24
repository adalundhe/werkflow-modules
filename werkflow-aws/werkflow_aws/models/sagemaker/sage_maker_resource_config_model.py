from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_instance_group_model import SageMakerInstanceGroupModel
from .sage_maker_instance_placement_config_model import SageMakerInstancePlacementConfigModel
from .sage_maker_instance_preference_model import SageMakerInstancePreferenceModel


class SageMakerResourceConfigModel(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    KeepAlivePeriodInSeconds: StrictInt | None = None
    InstanceGroups: list[SageMakerInstanceGroupModel] | None = None
    TrainingPlanArn: StrictStr | None = None
    InstancePlacementConfig: SageMakerInstancePlacementConfigModel | None = None
    InstancePreferences: list[SageMakerInstancePreferenceModel] | None = None
    SelectedInstanceType: StrictStr | None = None
    SelectedInstanceCount: StrictInt | None = None
