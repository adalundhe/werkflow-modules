from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMMaintenanceWindowExecution(BaseModel):
    WindowId: StrictStr | None = None
    WindowExecutionId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
