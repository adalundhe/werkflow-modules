from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .user import User


class ComponentWithIssueCount(BaseModel):
    assignee: User | None = None
    assigneeType: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    isAssigneeTypeValid: StrictBool | None = None
    issueCount: StrictInt | None = None
    lead: User | None = None
    name: StrictStr | None = None
    project: StrictStr | None = None
    projectId: StrictInt | None = None
    realAssignee: User | None = None
    realAssigneeType: StrictStr | None = None
    self: StrictStr | None = None
