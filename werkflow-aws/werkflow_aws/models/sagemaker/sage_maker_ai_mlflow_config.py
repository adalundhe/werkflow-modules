from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIMlflowConfig(BaseModel):
    MlflowResourceArn: StrictStr | None = None
    MlflowExperimentName: StrictStr | None = None
    MlflowRunName: StrictStr | None = None
