from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsInspectionDataRequest(BaseModel):
    protocol: StrictStr | None = None
    method: StrictStr | None = None
    url: StrictStr | None = None
    headers: StrictStr | None = None
    body: StrictStr | None = None
