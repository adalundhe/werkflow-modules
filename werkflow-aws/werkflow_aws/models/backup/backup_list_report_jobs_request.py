from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class BackupListReportJobsRequest(BaseModel):
    ByReportPlanName: StrictStr | None = None
    ByCreationBefore: datetime.datetime | StrictStr | None = None
    ByCreationAfter: datetime.datetime | StrictStr | None = None
    ByStatus: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
