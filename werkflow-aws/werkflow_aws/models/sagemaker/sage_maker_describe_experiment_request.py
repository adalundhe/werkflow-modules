from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeExperimentRequest(BaseModel):
    ExperimentName: StrictStr
