from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class ProjectPayload(BaseModel):
    fieldLayoutSchemeId: ProjectCreateResourceIdentifier | None = None
    issueSecuritySchemeId: ProjectCreateResourceIdentifier | None = None
    issueTypeSchemeId: ProjectCreateResourceIdentifier | None = None
    issueTypeScreenSchemeId: ProjectCreateResourceIdentifier | None = None
    notificationSchemeId: ProjectCreateResourceIdentifier | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    permissionSchemeId: ProjectCreateResourceIdentifier | None = None
    projectTypeKey: StrictStr | None = None
    workflowSchemeId: ProjectCreateResourceIdentifier | None = None
