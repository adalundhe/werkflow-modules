from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class StatusPayload(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    scope: StrictStr | None = None
    statusCategory: StrictStr | None = None
