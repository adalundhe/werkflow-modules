from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerParent(BaseModel):
    TrialName: StrictStr | None = None
    ExperimentName: StrictStr | None = None
