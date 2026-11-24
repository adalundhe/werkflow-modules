from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectRoleGroup(BaseModel):
    displayName: StrictStr | None = None
    groupId: StrictStr | None = None
    name: StrictStr | None = None
