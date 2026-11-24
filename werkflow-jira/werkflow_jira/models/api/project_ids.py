from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectIds(BaseModel):
    projectIds: list[StrictStr] | None = None
