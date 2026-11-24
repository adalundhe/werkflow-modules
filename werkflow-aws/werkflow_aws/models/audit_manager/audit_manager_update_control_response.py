from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_control import AuditManagerControl


class AuditManagerUpdateControlResponse(BaseModel):
    control: AuditManagerControl | None = None
    ResponseMetadata: dict[str, Any] | None = None
