from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_assessment_report import AuditManagerAssessmentReport


class AuditManagerCreateAssessmentReportResponse(BaseModel):
    assessmentReport: AuditManagerAssessmentReport | None = None
    ResponseMetadata: dict[str, Any] | None = None
