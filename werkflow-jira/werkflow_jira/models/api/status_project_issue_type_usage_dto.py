from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_project_issue_type_usage_page import StatusProjectIssueTypeUsagePage


class StatusProjectIssueTypeUsageDTO(BaseModel):
    issueTypes: StatusProjectIssueTypeUsagePage | None = None
    projectId: StrictStr | None = None
    statusId: StrictStr | None = None
