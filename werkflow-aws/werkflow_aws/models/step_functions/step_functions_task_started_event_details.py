from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsTaskStartedEventDetails(BaseModel):
    resourceType: StrictStr | None = None
    resource: StrictStr | None = None
