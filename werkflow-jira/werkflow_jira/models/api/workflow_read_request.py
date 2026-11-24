from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_and_issue_type_pair import ProjectAndIssueTypePair


class WorkflowReadRequest(BaseModel):
    projectAndIssueTypes: list[ProjectAndIssueTypePair] | None = None
    workflowIds: list[StrictStr] | None = None
    workflowNames: list[StrictStr] | None = None
