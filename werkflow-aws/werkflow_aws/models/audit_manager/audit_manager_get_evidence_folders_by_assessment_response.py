from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_assessment_evidence_folder import AuditManagerAssessmentEvidenceFolder


class AuditManagerGetEvidenceFoldersByAssessmentResponse(BaseModel):
    evidenceFolders: list[AuditManagerAssessmentEvidenceFolder] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
