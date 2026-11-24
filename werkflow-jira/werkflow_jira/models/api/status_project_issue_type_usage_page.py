from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_project_issue_type_usage import StatusProjectIssueTypeUsage


class StatusProjectIssueTypeUsagePage(BaseModel):
    nextPageToken: StrictStr | None = None
    values: list[StatusProjectIssueTypeUsage] | None = None
