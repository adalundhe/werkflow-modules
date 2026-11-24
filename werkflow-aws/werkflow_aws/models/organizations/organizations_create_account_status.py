from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OrganizationsCreateAccountStatus(BaseModel):
    Id: StrictStr | None = None
    AccountName: StrictStr | None = None
    State: StrictStr | None = None
    RequestedTimestamp: datetime.datetime | StrictStr | None = None
    CompletedTimestamp: datetime.datetime | StrictStr | None = None
    AccountId: StrictStr | None = None
    GovCloudAccountId: StrictStr | None = None
    FailureReason: StrictStr | None = None
