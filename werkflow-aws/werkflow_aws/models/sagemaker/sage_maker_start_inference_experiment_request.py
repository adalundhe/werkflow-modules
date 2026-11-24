from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStartInferenceExperimentRequest(BaseModel):
    Name: StrictStr
