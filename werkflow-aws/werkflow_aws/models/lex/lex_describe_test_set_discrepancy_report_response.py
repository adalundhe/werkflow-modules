from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_test_set_discrepancy_errors import LexTestSetDiscrepancyErrors
from .lex_test_set_discrepancy_report_resource_target import LexTestSetDiscrepancyReportResourceTarget


class LexDescribeTestSetDiscrepancyReportResponse(BaseModel):
    testSetDiscrepancyReportId: StrictStr | None = None
    testSetId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    target: LexTestSetDiscrepancyReportResourceTarget | None = None
    testSetDiscrepancyReportStatus: StrictStr | None = None
    lastUpdatedDataTime: datetime.datetime | StrictStr | None = None
    testSetDiscrepancyTopErrors: LexTestSetDiscrepancyErrors | None = None
    testSetDiscrepancyRawOutputUrl: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
