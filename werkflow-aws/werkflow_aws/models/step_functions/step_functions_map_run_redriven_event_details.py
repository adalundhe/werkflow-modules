from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StepFunctionsMapRunRedrivenEventDetails(BaseModel):
    mapRunArn: StrictStr | None = None
    redriveCount: StrictInt | None = None
