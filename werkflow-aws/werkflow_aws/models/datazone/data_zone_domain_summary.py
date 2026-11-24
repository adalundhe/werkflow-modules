from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneDomainSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    arn: StrictStr | None = None
    managedAccountId: StrictStr | None = None
    status: StrictStr | None = None
    portalUrl: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    domainVersion: StrictStr | None = None
