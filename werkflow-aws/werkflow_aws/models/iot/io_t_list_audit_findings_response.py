from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_finding import IoTAuditFinding


class IoTListAuditFindingsResponse(BaseModel):
    findings: list[IoTAuditFinding] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
