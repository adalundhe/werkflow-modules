from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .project_role_group import ProjectRoleGroup
from .project_role_user import ProjectRoleUser


class RoleActor(BaseModel):
    actorGroup: ProjectRoleGroup | None = None
    actorUser: ProjectRoleUser | None = None
    avatarUrl: StrictStr | None = None
    displayName: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
