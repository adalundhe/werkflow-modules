from __future__ import annotations
from pydantic import BaseModel
from .jira_workflow import JiraWorkflow
from .jira_workflow_status import JiraWorkflowStatus


class WorkflowCreateResponse(BaseModel):
    statuses: list[JiraWorkflowStatus] | None = None
    workflows: list[JiraWorkflow] | None = None
