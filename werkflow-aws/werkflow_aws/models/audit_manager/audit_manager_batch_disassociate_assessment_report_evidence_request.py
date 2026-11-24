from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerBatchDisassociateAssessmentReportEvidenceRequest(BaseModel):
    assessmentId: StrictStr
    evidenceFolderId: StrictStr
    evidenceIds: list[StrictStr]
