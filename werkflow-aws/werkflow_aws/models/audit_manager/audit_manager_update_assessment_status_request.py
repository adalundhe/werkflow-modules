from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AuditManagerUpdateAssessmentStatusRequest(BaseModel):
    assessmentId: StrictStr
    status: Literal['ACTIVE', 'INACTIVE']
