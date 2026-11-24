from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchDomainMaintenanceDetails(BaseModel):
    MaintenanceId: StrictStr | None = None
    DomainName: StrictStr | None = None
    Action: StrictStr | None = None
    NodeId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
