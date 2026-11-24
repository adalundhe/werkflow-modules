from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPipelineExperimentConfig(BaseModel):
    ExperimentName: StrictStr | None = None
    TrialName: StrictStr | None = None
