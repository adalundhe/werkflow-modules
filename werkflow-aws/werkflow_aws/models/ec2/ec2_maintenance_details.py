from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2MaintenanceDetails(BaseModel):
    PendingMaintenance: StrictStr | None = None
    MaintenanceAutoAppliedAfter: datetime.datetime | StrictStr | None = None
    LastMaintenanceApplied: datetime.datetime | StrictStr | None = None
