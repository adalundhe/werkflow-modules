from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAssociateTrialComponentRequest(BaseModel):
    TrialComponentName: StrictStr
    TrialName: StrictStr
