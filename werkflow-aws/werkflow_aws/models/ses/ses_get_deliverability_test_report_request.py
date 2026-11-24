from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetDeliverabilityTestReportRequest(BaseModel):
    ReportId: StrictStr
