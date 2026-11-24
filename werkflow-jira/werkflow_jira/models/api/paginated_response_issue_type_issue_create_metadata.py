from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata


class PaginatedResponseIssueTypeIssueCreateMetadata(BaseModel):
    maxResults: StrictInt | None = None
    results: list[IssueTypeIssueCreateMetadata] | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
