from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerLastUpdateStatus(BaseModel):
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
