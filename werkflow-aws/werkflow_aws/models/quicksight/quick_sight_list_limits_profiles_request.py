from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightListLimitsProfilesRequest(BaseModel):
    accountId: StrictStr
    resourceType: Literal['INDEX_STORAGE', 'AGENT_HOURS'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
