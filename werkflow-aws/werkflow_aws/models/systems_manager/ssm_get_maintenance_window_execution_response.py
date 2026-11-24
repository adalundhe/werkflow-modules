from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMGetMaintenanceWindowExecutionResponse(BaseModel):
    WindowExecutionId: StrictStr | None = None
    TaskIds: list[StrictStr] | None = None
    Status: StrictStr | None = None
    StatusDetails: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
