from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_deliverability_test_report import SESDeliverabilityTestReport


class SESListDeliverabilityTestReportsResponse(BaseModel):
    DeliverabilityTestReports: list[SESDeliverabilityTestReport] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
