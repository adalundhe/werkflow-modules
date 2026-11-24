from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class TabPayload(BaseModel):
    fields: list[ProjectCreateResourceIdentifier] | None = None
    name: StrictStr | None = None
