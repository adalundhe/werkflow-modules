from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class IssueTypeHierarchyPayload(BaseModel):
    hierarchyLevel: StrictInt | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
