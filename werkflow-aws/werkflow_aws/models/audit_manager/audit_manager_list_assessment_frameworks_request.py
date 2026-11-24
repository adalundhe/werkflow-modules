from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListAssessmentFrameworksRequest(BaseModel):
    frameworkType: Literal['Standard', 'Custom']
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
