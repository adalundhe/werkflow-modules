from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateTrialRequest(BaseModel):
    TrialName: StrictStr
    DisplayName: StrictStr | None = None
