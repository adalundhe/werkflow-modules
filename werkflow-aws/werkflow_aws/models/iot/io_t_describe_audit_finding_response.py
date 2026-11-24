from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_audit_finding import IoTAuditFinding


class IoTDescribeAuditFindingResponse(BaseModel):
    finding: IoTAuditFinding | None = None
    ResponseMetadata: dict[str, Any] | None = None
