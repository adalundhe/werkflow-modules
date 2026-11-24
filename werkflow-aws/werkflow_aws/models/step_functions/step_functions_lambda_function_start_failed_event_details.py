from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsLambdaFunctionStartFailedEventDetails(BaseModel):
    error: StrictStr | None = None
    cause: StrictStr | None = None
