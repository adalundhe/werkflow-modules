from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class Route53DomainsGetOperationDetailResponse(BaseModel):
    OperationId: StrictStr | None = None
    Status: StrictStr | None = None
    Message: StrictStr | None = None
    DomainName: StrictStr | None = None
    Type: StrictStr | None = None
    SubmittedDate: datetime.datetime | StrictStr | None = None
    LastUpdatedDate: datetime.datetime | StrictStr | None = None
    StatusFlag: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
