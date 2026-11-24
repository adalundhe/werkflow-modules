from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerDisassociateAssessmentReportEvidenceFolderRequest(BaseModel):
    assessmentId: StrictStr
    evidenceFolderId: StrictStr
