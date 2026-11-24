from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class UserFilter(BaseModel):
    enabled: StrictBool | None = None
    groups: list[StrictStr] | None = None
    roleIds: list[StrictInt] | None = None
