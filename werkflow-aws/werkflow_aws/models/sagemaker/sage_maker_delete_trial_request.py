from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteTrialRequest(BaseModel):
    TrialName: StrictStr
