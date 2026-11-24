from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_framework import AuditManagerFramework


class AuditManagerUpdateAssessmentFrameworkResponse(BaseModel):
    framework: AuditManagerFramework | None = None
    ResponseMetadata: dict[str, Any] | None = None
