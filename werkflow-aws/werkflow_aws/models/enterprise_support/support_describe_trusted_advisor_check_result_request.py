from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportDescribeTrustedAdvisorCheckResultRequest(BaseModel):
    checkId: StrictStr
    language: StrictStr | None = None
