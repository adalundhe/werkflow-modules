from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_assessment_framework_share_request import AuditManagerAssessmentFrameworkShareRequest


class AuditManagerUpdateAssessmentFrameworkShareResponse(BaseModel):
    assessmentFrameworkShareRequest: AuditManagerAssessmentFrameworkShareRequest | None = None
    ResponseMetadata: dict[str, Any] | None = None
