from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLPartialFailureReason(BaseModel):
    PartialFailureMessage: StrictStr | None = None
