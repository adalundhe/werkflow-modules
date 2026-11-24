from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsInspectionDataResponse(BaseModel):
    protocol: StrictStr | None = None
    statusCode: StrictStr | None = None
    statusMessage: StrictStr | None = None
    headers: StrictStr | None = None
    body: StrictStr | None = None
