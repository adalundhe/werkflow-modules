from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ProjectRoleActorsUpdateBean(BaseModel):
    categorisedActors: dict[StrictStr, list[StrictStr]] | None = None
    id: StrictInt | None = None
