from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class RolePayload(BaseModel):
    defaultActors: list[ProjectCreateResourceIdentifier] | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    type: StrictStr | None = None
