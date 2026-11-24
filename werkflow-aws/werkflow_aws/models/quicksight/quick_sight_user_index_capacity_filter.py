from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_capacity_bytes_range_filter import QuickSightCapacityBytesRangeFilter
from .quick_sight_user_name_or_email_filter import QuickSightUserNameOrEmailFilter


class QuickSightUserIndexCapacityFilter(BaseModel):
    userNameOrEmail: QuickSightUserNameOrEmailFilter | None = None
    totalCapacityBytes: QuickSightCapacityBytesRangeFilter | None = None
