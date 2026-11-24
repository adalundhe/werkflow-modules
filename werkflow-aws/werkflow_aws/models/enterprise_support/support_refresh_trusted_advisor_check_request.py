from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportRefreshTrustedAdvisorCheckRequest(BaseModel):
    checkId: StrictStr
