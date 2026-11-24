from __future__ import annotations
from pydantic import BaseModel
from .jira_workflow_preview_status import JiraWorkflowPreviewStatus
from .workflow_preview import WorkflowPreview


class WorkflowPreviewResponse(BaseModel):
    statuses: list[JiraWorkflowPreviewStatus] | None = None
    workflows: list[WorkflowPreview] | None = None
