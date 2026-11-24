from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_assessment import AuditManagerAssessment


class AuditManagerCreateAssessmentResponse(BaseModel):
    assessment: AuditManagerAssessment | None = None
    ResponseMetadata: dict[str, Any] | None = None
