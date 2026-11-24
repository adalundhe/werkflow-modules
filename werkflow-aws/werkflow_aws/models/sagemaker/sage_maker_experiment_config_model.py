from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerExperimentConfigModel(BaseModel):
    ExperimentName: StrictStr | None = None
    TrialName: StrictStr | None = None
    TrialComponentDisplayName: StrictStr | None = None
    RunName: StrictStr | None = None
