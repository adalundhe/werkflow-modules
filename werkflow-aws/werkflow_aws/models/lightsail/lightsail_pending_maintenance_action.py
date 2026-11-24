from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailPendingMaintenanceAction(BaseModel):
    action: StrictStr | None = None
    description: StrictStr | None = None
    currentApplyDate: datetime.datetime | StrictStr | None = None
