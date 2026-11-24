from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsMapRunStartedEventDetails(BaseModel):
    mapRunArn: StrictStr | None = None
