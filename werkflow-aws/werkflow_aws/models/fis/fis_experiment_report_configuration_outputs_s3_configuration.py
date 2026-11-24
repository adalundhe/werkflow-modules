from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentReportConfigurationOutputsS3Configuration(BaseModel):
    bucketName: StrictStr | None = None
    prefix: StrictStr | None = None
