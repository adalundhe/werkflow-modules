from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessUsersAndGroups(BaseModel):
    userIds: list[StrictStr] | None = None
    userGroups: list[StrictStr] | None = None
