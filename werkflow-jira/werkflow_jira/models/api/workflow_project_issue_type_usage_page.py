from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_project_issue_type_usage import WorkflowProjectIssueTypeUsage


class WorkflowProjectIssueTypeUsagePage(BaseModel):
    nextPageToken: StrictStr | None = None
    values: list[WorkflowProjectIssueTypeUsage] | None = None
