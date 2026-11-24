from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeTestSetDiscrepancyReportRequest(BaseModel):
    testSetDiscrepancyReportId: StrictStr
