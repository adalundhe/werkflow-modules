from __future__ import annotations
from pydantic import BaseModel
from .found_groups import FoundGroups
from .found_users import FoundUsers


class FoundUsersAndGroups(BaseModel):
    groups: FoundGroups | None = None
    users: FoundUsers | None = None
