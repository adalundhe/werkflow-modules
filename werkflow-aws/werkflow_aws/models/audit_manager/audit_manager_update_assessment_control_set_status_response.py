from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_assessment_control_set import AuditManagerAssessmentControlSet


class AuditManagerUpdateAssessmentControlSetStatusResponse(BaseModel):
    controlSet: AuditManagerAssessmentControlSet | None = None
    ResponseMetadata: dict[str, Any] | None = None
