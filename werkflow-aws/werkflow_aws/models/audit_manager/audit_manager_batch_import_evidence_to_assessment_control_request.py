from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_manual_evidence import AuditManagerManualEvidence


class AuditManagerBatchImportEvidenceToAssessmentControlRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    controlId: StrictStr
    manualEvidence: list[AuditManagerManualEvidence]
