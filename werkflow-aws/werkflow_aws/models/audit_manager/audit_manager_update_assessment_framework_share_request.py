from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AuditManagerUpdateAssessmentFrameworkShareRequest(BaseModel):
    requestId: StrictStr
    requestType: Literal['SENT', 'RECEIVED']
    action: Literal['ACCEPT', 'DECLINE', 'REVOKE']
