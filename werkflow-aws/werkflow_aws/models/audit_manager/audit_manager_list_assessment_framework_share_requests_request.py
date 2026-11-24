from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListAssessmentFrameworkShareRequestsRequest(BaseModel):
    requestType: Literal['SENT', 'RECEIVED']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
