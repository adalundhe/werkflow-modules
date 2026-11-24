from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportDescribeTrustedAdvisorCheckSummariesRequest(BaseModel):
    checkIds: list[StrictStr]
