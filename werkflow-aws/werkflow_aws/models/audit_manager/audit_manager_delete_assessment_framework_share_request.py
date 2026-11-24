from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AuditManagerDeleteAssessmentFrameworkShareRequest(BaseModel):
    requestId: StrictStr
    requestType: Literal['SENT', 'RECEIVED']
