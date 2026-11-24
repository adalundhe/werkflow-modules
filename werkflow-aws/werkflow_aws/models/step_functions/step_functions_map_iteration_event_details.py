from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsMapIterationEventDetails(BaseModel):
    name: StrictStr | None = None
    index: StrictInt | None = None
