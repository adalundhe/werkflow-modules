from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentReportError(BaseModel):
    code: StrictStr | None = None
