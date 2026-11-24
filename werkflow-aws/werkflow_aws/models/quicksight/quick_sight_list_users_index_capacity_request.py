from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_user_index_capacity_filter import QuickSightUserIndexCapacityFilter


class QuickSightListUsersIndexCapacityRequest(BaseModel):
    awsAccountId: StrictStr
    namespace: StrictStr | None = None
    filters: list[QuickSightUserIndexCapacityFilter] | None = None
    sortBy: Literal['TOTAL_CAPACITY_BYTES'] | None = None
    sortOrder: Literal['ASC', 'DESC'] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
