from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_settings import AuditManagerSettings


class AuditManagerUpdateSettingsResponse(BaseModel):
    settings: AuditManagerSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
