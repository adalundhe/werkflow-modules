from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RedshiftDeferredMaintenanceWindow(BaseModel):
    DeferMaintenanceIdentifier: StrictStr | None = None
    DeferMaintenanceStartTime: datetime.datetime | StrictStr | None = None
    DeferMaintenanceEndTime: datetime.datetime | StrictStr | None = None
