from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListAssessmentsRequest(BaseModel):
    status: Literal['ACTIVE', 'INACTIVE'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
