from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .issue_type_info import IssueTypeInfo


class ProjectIssueTypesHierarchyLevel(BaseModel):
    entityId: StrictStr | None = None
    issueTypes: list[IssueTypeInfo] | None = None
    level: StrictInt | None = None
    name: StrictStr | None = None
