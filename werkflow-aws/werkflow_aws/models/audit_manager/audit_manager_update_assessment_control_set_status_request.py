from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AuditManagerUpdateAssessmentControlSetStatusRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr
    status: Literal['ACTIVE', 'UNDER_REVIEW', 'REVIEWED']
    comment: StrictStr
