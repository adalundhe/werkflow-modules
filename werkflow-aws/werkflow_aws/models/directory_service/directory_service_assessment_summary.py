from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceAssessmentSummary(BaseModel):
    AssessmentId: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    DnsName: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    LastUpdateDateTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    CustomerDnsIps: list[StrictStr] | None = None
    ReportType: StrictStr | None = None
