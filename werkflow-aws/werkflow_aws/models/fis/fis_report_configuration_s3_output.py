from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISReportConfigurationS3Output(BaseModel):
    bucketName: StrictStr | None = None
    prefix: StrictStr | None = None
