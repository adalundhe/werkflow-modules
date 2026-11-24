from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_task_metadata import IoTAuditTaskMetadata


class IoTListAuditTasksResponse(BaseModel):
    tasks: list[IoTAuditTaskMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
