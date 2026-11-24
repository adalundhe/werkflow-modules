from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeInferenceExperimentRequest(BaseModel):
    Name: StrictStr
