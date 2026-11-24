from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerBatchAssociateAssessmentReportEvidenceRequest(BaseModel):
    assessmentId: StrictStr
    evidenceFolderId: StrictStr
    evidenceIds: list[StrictStr]
