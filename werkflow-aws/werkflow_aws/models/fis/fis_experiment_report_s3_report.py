from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentReportS3Report(BaseModel):
    arn: StrictStr | None = None
    reportType: StrictStr | None = None
