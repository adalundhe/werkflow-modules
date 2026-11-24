from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_training_instance_type import SageMakerTrainingInstanceType


class SageMakerInstancePreference(BaseModel):
    InstanceType: SageMakerTrainingInstanceType | None = None
    InstanceCount: StrictInt | None = None
    TrainingPlanArns: list[StrictStr] | None = None
