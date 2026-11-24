from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMLflowConfiguration(BaseModel):
    MlflowResourceArn: StrictStr | None = None
    MlflowExperimentName: StrictStr | None = None
