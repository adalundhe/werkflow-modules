from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_user_limits_entry import QuickSightUserLimitsEntry


class QuickSightBatchDescribeUserLimitsRequest(BaseModel):
    accountId: StrictStr
    users: list[QuickSightUserLimitsEntry] | None = None
    resourceTypes: list[Literal['INDEX_STORAGE', 'AGENT_HOURS']] | None = None
