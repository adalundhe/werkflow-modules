from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteTrialComponentRequest(BaseModel):
    TrialComponentName: StrictStr
