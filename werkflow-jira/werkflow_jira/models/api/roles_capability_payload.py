from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .role_payload import RolePayload


class RolesCapabilityPayload(BaseModel):
    roleToProjectActors: dict[StrictStr, list[ProjectCreateResourceIdentifier]] | None = None
    roles: list[RolePayload] | None = None
