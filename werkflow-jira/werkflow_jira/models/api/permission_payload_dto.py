from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .permission_grant_dto import PermissionGrantDTO
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class PermissionPayloadDTO(BaseModel):
    addAddonRole: StrictBool | None = None
    description: StrictStr | None = None
    grants: list[PermissionGrantDTO] | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
