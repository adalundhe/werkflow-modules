from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLCandidateStep(BaseModel):
    CandidateStepType: StrictStr | None = None
    CandidateStepArn: StrictStr | None = None
    CandidateStepName: StrictStr | None = None
