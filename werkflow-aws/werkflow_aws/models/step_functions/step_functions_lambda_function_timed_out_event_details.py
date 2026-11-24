from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsLambdaFunctionTimedOutEventDetails(BaseModel):
    error: StrictStr | None = None
    cause: StrictStr | None = None
