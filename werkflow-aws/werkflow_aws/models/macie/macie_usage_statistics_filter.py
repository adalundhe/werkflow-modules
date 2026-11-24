from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieUsageStatisticsFilter(BaseModel):
    comparator: Literal['GT', 'GTE', 'LT', 'LTE', 'EQ', 'NE', 'CONTAINS'] | None = None
    key: Literal['accountId', 'serviceLimit', 'freeTrialStartDate', 'total'] | None = None
    values: list[StrictStr] | None = None
