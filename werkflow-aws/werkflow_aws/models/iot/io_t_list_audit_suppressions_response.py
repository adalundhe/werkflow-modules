from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_suppression import IoTAuditSuppression


class IoTListAuditSuppressionsResponse(BaseModel):
    suppressions: list[IoTAuditSuppression] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
