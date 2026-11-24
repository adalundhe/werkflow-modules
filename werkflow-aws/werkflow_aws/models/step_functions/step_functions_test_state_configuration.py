from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsTestStateConfiguration(BaseModel):
    retrierRetryCount: StrictInt | None = None
    errorCausedByState: StrictStr | None = None
    mapIterationFailureCount: StrictInt | None = None
    mapItemReaderData: StrictStr | None = None
