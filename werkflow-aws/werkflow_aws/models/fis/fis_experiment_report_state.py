from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fis_experiment_report_error import FISExperimentReportError


class FISExperimentReportState(BaseModel):
    status: StrictStr | None = None
    reason: StrictStr | None = None
    error: FISExperimentReportError | None = None
