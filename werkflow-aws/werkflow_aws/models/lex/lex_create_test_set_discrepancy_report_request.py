from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_test_set_discrepancy_report_resource_target import LexTestSetDiscrepancyReportResourceTarget


class LexCreateTestSetDiscrepancyReportRequest(BaseModel):
    testSetId: StrictStr
    target: LexTestSetDiscrepancyReportResourceTarget
