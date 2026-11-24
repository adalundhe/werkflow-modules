from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_assessment_control import AuditManagerAssessmentControl


class AuditManagerUpdateAssessmentControlResponse(BaseModel):
    control: AuditManagerAssessmentControl | None = None
    ResponseMetadata: dict[str, Any] | None = None
