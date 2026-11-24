from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ImageUsageReportEntry(BaseModel):
    ResourceType: StrictStr | None = None
    ReportId: StrictStr | None = None
    UsageCount: StrictInt | None = None
    AccountId: StrictStr | None = None
    ImageId: StrictStr | None = None
    ReportCreationTime: datetime.datetime | StrictStr | None = None
