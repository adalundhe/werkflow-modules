from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_user_index_capacity import QuickSightUserIndexCapacity


class QuickSightListUsersIndexCapacityResponse(BaseModel):
    users: list[QuickSightUserIndexCapacity] | None = None
    nextToken: StrictStr | None = None
    requestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
