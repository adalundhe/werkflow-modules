from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESDeliverabilityTestReport(BaseModel):
    ReportId: StrictStr | None = None
    ReportName: StrictStr | None = None
    Subject: StrictStr | None = None
    FromEmailAddress: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    DeliverabilityTestStatus: StrictStr | None = None
