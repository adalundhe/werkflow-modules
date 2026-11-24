from __future__ import annotations
from pydantic import BaseModel
from .issue_bean import IssueBean
from .issue_error import IssueError


class BulkIssueResults(BaseModel):
    issueErrors: list[IssueError] | None = None
    issues: list[IssueBean] | None = None
