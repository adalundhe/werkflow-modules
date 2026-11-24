from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_set_discrepancy_report_resource_target import LexTestSetDiscrepancyReportResourceTarget


class LexCreateTestSetDiscrepancyReportResponse(BaseModel):
    testSetDiscrepancyReportId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    testSetId: StrictStr | None = None
    target: LexTestSetDiscrepancyReportResourceTarget | None = None
    ResponseMetadata: dict[str, Any] | None = None
