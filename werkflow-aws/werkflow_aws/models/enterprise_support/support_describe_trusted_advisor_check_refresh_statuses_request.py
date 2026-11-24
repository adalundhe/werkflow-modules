from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportDescribeTrustedAdvisorCheckRefreshStatusesRequest(BaseModel):
    checkIds: list[StrictStr]
