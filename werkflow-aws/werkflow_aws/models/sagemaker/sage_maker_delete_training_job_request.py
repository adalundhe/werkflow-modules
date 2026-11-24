from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteTrainingJobRequest(BaseModel):
    TrainingJobName: StrictStr
