from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeHyperParameterTuningJobRequest(BaseModel):
    HyperParameterTuningJobName: StrictStr
