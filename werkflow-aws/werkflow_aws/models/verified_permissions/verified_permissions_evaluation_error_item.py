from __future__ import annotations
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsEvaluationErrorItem(BaseModel):
    errorDescription: StrictStr | None = None
