from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMlflowDetails(BaseModel):
    MlflowExperimentId: StrictStr | None = None
    MlflowRunId: StrictStr | None = None
