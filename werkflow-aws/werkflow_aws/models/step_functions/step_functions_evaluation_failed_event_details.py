from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsEvaluationFailedEventDetails(BaseModel):
    error: StrictStr | None = None
    cause: StrictStr | None = None
    location: StrictStr | None = None
    state: StrictStr | None = None
