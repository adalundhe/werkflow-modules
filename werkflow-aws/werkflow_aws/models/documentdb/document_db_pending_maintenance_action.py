from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DocumentDBPendingMaintenanceAction(BaseModel):
    Action: StrictStr | None = None
    AutoAppliedAfterDate: datetime.datetime | StrictStr | None = None
    ForcedApplyDate: datetime.datetime | StrictStr | None = None
    OptInStatus: StrictStr | None = None
    CurrentApplyDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
