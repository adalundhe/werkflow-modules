from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeTrainingSessionRequest(BaseModel):
    TrainingSessionName: StrictStr
