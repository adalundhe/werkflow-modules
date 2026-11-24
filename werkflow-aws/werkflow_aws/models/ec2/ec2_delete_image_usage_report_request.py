from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteImageUsageReportRequest(BaseModel):
    ReportId: StrictStr
    DryRun: StrictBool | None = None
