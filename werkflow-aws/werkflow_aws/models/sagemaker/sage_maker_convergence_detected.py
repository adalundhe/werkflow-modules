from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerConvergenceDetected(BaseModel):
    CompleteOnConvergence: StrictStr | None = None
