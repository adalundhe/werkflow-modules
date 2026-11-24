from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class Route53DomainsOperationSummary(BaseModel):
    OperationId: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    SubmittedDate: datetime.datetime | StrictStr | None = None
    DomainName: StrictStr | None = None
    Message: StrictStr | None = None
    StatusFlag: StrictStr | None = None
    LastUpdatedDate: datetime.datetime | StrictStr | None = None
