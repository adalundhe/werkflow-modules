from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeTrainingPlanRequest(BaseModel):
    TrainingPlanName: StrictStr
