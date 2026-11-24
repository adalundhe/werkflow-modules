from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteTrainingSessionRequest(BaseModel):
    TrainingSessionName: StrictStr
