from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .group_name import GroupName
from .project import Project
from .project_role import ProjectRole
from .user_bean import UserBean


class SharePermission(BaseModel):
    group: GroupName | None = None
    id: StrictInt | None = None
    project: Project | None = None
    role: ProjectRole | None = None
    type: StrictStr | None = None
    user: UserBean | None = None
