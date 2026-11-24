from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class UpdateProjectDetails(BaseModel):
    assigneeType: StrictStr | None = None
    avatarId: StrictInt | None = None
    categoryId: StrictInt | None = None
    description: StrictStr | None = None
    issueSecurityScheme: StrictInt | None = None
    key: StrictStr | None = None
    lead: StrictStr | None = None
    leadAccountId: StrictStr | None = None
    name: StrictStr | None = None
    notificationScheme: StrictInt | None = None
    permissionScheme: StrictInt | None = None
    releasedProjectKeys: list[StrictStr] | None = None
    url: StrictStr | None = None
