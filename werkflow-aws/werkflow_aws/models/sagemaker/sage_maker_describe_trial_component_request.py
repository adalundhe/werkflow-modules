from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeTrialComponentRequest(BaseModel):
    TrialComponentName: StrictStr
