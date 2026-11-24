from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_scheduled_audit_metadata import IoTScheduledAuditMetadata


class IoTListScheduledAuditsResponse(BaseModel):
    scheduledAudits: list[IoTScheduledAuditMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
