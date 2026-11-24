from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrialComponentStatus(BaseModel):
    PrimaryStatus: StrictStr | None = None
    Message: StrictStr | None = None
