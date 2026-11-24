from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class ToLayoutPayload(BaseModel):
    port: StrictInt | None = None
    status: ProjectCreateResourceIdentifier | None = None
