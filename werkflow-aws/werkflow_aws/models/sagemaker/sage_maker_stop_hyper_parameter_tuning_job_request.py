from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerStopHyperParameterTuningJobRequest(BaseModel):
    HyperParameterTuningJobName: StrictStr
