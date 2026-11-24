from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class FromLayoutPayload(BaseModel):
    fromPort: StrictInt | None = None
    status: ProjectCreateResourceIdentifier | None = None
    toPortOverride: StrictInt | None = None
