from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .group_name import GroupName
from .user import User


class FilterSubscription(BaseModel):
    group: GroupName | None = None
    id: StrictInt | None = None
    user: User | None = None
