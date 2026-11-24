from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSbomValidationResultSummary(BaseModel):
    fileName: StrictStr | None = None
    validationResult: StrictStr | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
