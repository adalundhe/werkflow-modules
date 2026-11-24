from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_report_evidence_error import AuditManagerAssessmentReportEvidenceError


class AuditManagerBatchDisassociateAssessmentReportEvidenceResponse(BaseModel):
    evidenceIds: list[StrictStr] | None = None
    errors: list[AuditManagerAssessmentReportEvidenceError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
