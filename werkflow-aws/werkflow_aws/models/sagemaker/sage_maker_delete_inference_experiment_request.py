from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteInferenceExperimentRequest(BaseModel):
    Name: StrictStr
