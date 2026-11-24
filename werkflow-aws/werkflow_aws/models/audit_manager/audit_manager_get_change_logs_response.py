from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_change_log import AuditManagerChangeLog


class AuditManagerGetChangeLogsResponse(BaseModel):
    changeLogs: list[AuditManagerChangeLog] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
