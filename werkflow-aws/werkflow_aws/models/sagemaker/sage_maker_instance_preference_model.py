from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerInstancePreferenceModel(BaseModel):
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    TrainingPlanArns: list[StrictStr] | None = None
