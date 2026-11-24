from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerAssociateAssessmentReportEvidenceFolderRequest(BaseModel):
    assessmentId: StrictStr
    evidenceFolderId: StrictStr
