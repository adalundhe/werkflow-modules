from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class IssueTypeSchemePayload(BaseModel):
    defaultIssueTypeId: ProjectCreateResourceIdentifier | None = None
    description: StrictStr | None = None
    issueTypeIds: list[ProjectCreateResourceIdentifier] | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
