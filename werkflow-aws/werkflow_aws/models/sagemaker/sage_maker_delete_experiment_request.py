from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteExperimentRequest(BaseModel):
    ExperimentName: StrictStr
