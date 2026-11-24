from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SSMMaintenanceWindowExecutionTaskInvocationIdentity(BaseModel):
    WindowExecutionId: StrictStr | None = None
    TaskExecutionId: StrictStr | None = None
    InvocationId: StrictStr | None = None
    ExecutionId: StrictStr | None = None
    TaskType: StrictStr | None = None
    Parameters: StrictStr | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    OwnerInformation: StrictStr | None = None
    WindowTargetId: StrictStr | None = None
