from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SESCreateDeliverabilityTestReportResponse(BaseModel):
    ReportId: StrictStr | None = None
    DeliverabilityTestStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
