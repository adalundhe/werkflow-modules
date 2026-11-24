from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_change_log import IssueChangeLog


class BulkChangelogResponseBean(BaseModel):
    issueChangeLogs: list[IssueChangeLog] | None = None
    nextPageToken: StrictStr | None = None
