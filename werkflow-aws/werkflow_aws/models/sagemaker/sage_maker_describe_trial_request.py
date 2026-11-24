from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeTrialRequest(BaseModel):
    TrialName: StrictStr
