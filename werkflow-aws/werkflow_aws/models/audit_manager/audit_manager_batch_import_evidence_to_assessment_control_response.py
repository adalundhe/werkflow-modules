from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_batch_import_evidence_to_assessment_control_error import AuditManagerBatchImportEvidenceToAssessmentControlError


class AuditManagerBatchImportEvidenceToAssessmentControlResponse(BaseModel):
    errors: list[AuditManagerBatchImportEvidenceToAssessmentControlError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
