from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCleanupFailure(BaseModel):
    StepName: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
