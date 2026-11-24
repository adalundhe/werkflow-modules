from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneProjectProfileSummary(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    status: StrictStr | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    domainUnitId: StrictStr | None = None
