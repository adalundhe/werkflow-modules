from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_manual_evidence import AuditManagerManualEvidence


class AuditManagerBatchImportEvidenceToAssessmentControlError(BaseModel):
    manualEvidence: AuditManagerManualEvidence | None = None
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
