from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsTaskTimedOutEventDetails(BaseModel):
    resourceType: StrictStr | None = None
    resource: StrictStr | None = None
    error: StrictStr | None = None
    cause: StrictStr | None = None
