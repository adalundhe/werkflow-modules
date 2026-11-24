from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MacieUsageStatisticsSortBy(BaseModel):
    key: Literal['accountId', 'total', 'serviceLimitValue', 'freeTrialStartDate'] | None = None
    orderBy: Literal['ASC', 'DESC'] | None = None
