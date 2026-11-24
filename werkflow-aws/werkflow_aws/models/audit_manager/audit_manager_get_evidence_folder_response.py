from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_assessment_evidence_folder import AuditManagerAssessmentEvidenceFolder


class AuditManagerGetEvidenceFolderResponse(BaseModel):
    evidenceFolder: AuditManagerAssessmentEvidenceFolder | None = None
    ResponseMetadata: dict[str, Any] | None = None
