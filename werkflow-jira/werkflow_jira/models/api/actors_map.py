from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ActorsMap(BaseModel):
    group: list[StrictStr] | None = None
    groupId: list[StrictStr] | None = None
    user: list[StrictStr] | None = None
