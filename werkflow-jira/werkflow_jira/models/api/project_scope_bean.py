from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ProjectScopeBean(BaseModel):
    attributes: list[StrictStr] | None = None
    id: StrictInt | None = None
