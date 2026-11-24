from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateExperimentRequest(BaseModel):
    ExperimentName: StrictStr
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
