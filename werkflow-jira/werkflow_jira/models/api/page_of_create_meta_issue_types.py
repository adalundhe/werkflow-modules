from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt
from .issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata


class PageOfCreateMetaIssueTypes(BaseModel):
    model_config = ConfigDict(extra="allow")

    createMetaIssueType: list[IssueTypeIssueCreateMetadata] | None = None
    issueTypes: list[IssueTypeIssueCreateMetadata] | None = None
    maxResults: StrictInt | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
