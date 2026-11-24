from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class ScreenSchemePayload(BaseModel):
    defaultScreen: ProjectCreateResourceIdentifier | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    screens: dict[StrictStr, ProjectCreateResourceIdentifier] | None = None
