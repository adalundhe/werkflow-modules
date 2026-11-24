from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class PermissionGrantDTO(BaseModel):
    applicationAccess: list[StrictStr] | None = None
    groupCustomFields: list[ProjectCreateResourceIdentifier] | None = None
    groups: list[ProjectCreateResourceIdentifier] | None = None
    permissionKeys: list[StrictStr] | None = None
    projectRoles: list[ProjectCreateResourceIdentifier] | None = None
    specialGrants: list[StrictStr] | None = None
    userCustomFields: list[ProjectCreateResourceIdentifier] | None = None
    users: list[ProjectCreateResourceIdentifier] | None = None
