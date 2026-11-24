from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .jira_workflow import JiraWorkflow
from .jira_workflow_status import JiraWorkflowStatus


class WorkflowUpdateResponse(BaseModel):
    statuses: list[JiraWorkflowStatus] | None = None
    taskId: StrictStr | None = None
    workflows: list[JiraWorkflow] | None = None
