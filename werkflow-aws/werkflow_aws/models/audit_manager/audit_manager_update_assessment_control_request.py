from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AuditManagerUpdateAssessmentControlRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    controlId: StrictStr
    controlStatus: Literal['UNDER_REVIEW', 'REVIEWED', 'INACTIVE'] | None = None
    commentBody: StrictStr | None = None
