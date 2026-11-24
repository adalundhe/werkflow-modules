from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceEvaluationStatus(BaseModel):
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
