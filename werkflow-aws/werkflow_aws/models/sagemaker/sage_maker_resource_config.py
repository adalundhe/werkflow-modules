from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_instance_group import SageMakerInstanceGroup
from .sage_maker_instance_placement_config import SageMakerInstancePlacementConfig
from .sage_maker_instance_preference import SageMakerInstancePreference
from .sage_maker_training_instance_type import SageMakerTrainingInstanceType


class SageMakerResourceConfig(BaseModel):
    InstanceType: SageMakerTrainingInstanceType | None = None
    InstanceCount: StrictInt | None = None
    VolumeSizeInGB: StrictInt | None = None
    VolumeKmsKeyId: StrictStr | None = None
    KeepAlivePeriodInSeconds: StrictInt | None = None
    InstanceGroups: list[SageMakerInstanceGroup] | None = None
    TrainingPlanArn: StrictStr | None = None
    InstancePlacementConfig: SageMakerInstancePlacementConfig | None = None
    InstancePreferences: list[SageMakerInstancePreference] | None = None
    SelectedInstanceType: SageMakerTrainingInstanceType | None = None
    SelectedInstanceCount: StrictInt | None = None
