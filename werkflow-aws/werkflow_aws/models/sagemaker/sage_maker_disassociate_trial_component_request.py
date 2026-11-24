from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDisassociateTrialComponentRequest(BaseModel):
    TrialComponentName: StrictStr
    TrialName: StrictStr
