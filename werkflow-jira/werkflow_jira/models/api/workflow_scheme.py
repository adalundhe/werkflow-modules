from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .issue_type_details import IssueTypeDetails
from .user import User


class WorkflowScheme(BaseModel):
    defaultWorkflow: StrictStr | None = None
    description: StrictStr | None = None
    draft: StrictBool | None = None
    id: StrictInt | None = None
    issueTypeMappings: dict[StrictStr, StrictStr] | None = None
    issueTypes: dict[StrictStr, IssueTypeDetails] | None = None
    lastModified: StrictStr | None = None
    lastModifiedUser: User | None = None
    name: StrictStr | None = None
    originalDefaultWorkflow: StrictStr | None = None
    originalIssueTypeMappings: dict[StrictStr, StrictStr] | None = None
    self: StrictStr | None = None
    updateDraftIfNeeded: StrictBool | None = None
