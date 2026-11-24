from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CreateProjectDetails(BaseModel):
    assigneeType: StrictStr | None = None
    avatarId: StrictInt | None = None
    categoryId: StrictInt | None = None
    description: StrictStr | None = None
    fieldConfigurationScheme: StrictInt | None = None
    fieldScheme: StrictInt | None = None
    issueSecurityScheme: StrictInt | None = None
    issueTypeScheme: StrictInt | None = None
    issueTypeScreenScheme: StrictInt | None = None
    key: StrictStr | None = None
    lead: StrictStr | None = None
    leadAccountId: StrictStr | None = None
    name: StrictStr | None = None
    notificationScheme: StrictInt | None = None
    permissionScheme: StrictInt | None = None
    projectTemplateKey: StrictStr | None = None
    projectTypeKey: StrictStr | None = None
    url: StrictStr | None = None
    workflowScheme: StrictInt | None = None
