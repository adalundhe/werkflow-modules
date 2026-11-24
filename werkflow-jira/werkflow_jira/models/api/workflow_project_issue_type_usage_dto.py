from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_project_issue_type_usage_page import WorkflowProjectIssueTypeUsagePage


class WorkflowProjectIssueTypeUsageDTO(BaseModel):
    issueTypes: WorkflowProjectIssueTypeUsagePage | None = None
    projectId: StrictStr | None = None
    workflowId: StrictStr | None = None
