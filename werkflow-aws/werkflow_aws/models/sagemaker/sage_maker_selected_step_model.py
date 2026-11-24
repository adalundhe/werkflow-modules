from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerSelectedStepModel(BaseModel):
    StepName: StrictStr | None = None
