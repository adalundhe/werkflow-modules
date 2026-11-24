from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportDescribeTrustedAdvisorChecksRequest(BaseModel):
    language: StrictStr
