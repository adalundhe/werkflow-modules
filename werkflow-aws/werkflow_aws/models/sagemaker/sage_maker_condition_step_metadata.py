from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerConditionStepMetadata(BaseModel):
    Outcome: StrictStr | None = None
