from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .jira_workflow import JiraWorkflow
from .jira_workflow_status import JiraWorkflowStatus


class WorkflowSearchResponse(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    statuses: list[JiraWorkflowStatus] | None = None
    total: StrictInt | None = None
    values: list[JiraWorkflow] | None = None
