from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTStartAuditMitigationActionsTaskResponse(BaseModel):
    taskId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
