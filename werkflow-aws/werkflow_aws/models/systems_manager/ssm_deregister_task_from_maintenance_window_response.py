from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMDeregisterTaskFromMaintenanceWindowResponse(BaseModel):
    WindowId: StrictStr | None = None
    WindowTaskId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
