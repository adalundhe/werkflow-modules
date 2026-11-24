from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .user import User


class ProjectComponent(BaseModel):
    ari: StrictStr | None = None
    assignee: User | None = None
    assigneeType: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    isAssigneeTypeValid: StrictBool | None = None
    lead: User | None = None
    leadAccountId: StrictStr | None = None
    leadUserName: StrictStr | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    name: StrictStr | None = None
    project: StrictStr | None = None
    projectId: StrictInt | None = None
    realAssignee: User | None = None
    realAssigneeType: StrictStr | None = None
    self: StrictStr | None = None
