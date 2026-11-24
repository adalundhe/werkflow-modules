from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_issue_create_metadata import ProjectIssueCreateMetadata


class IssueCreateMetadata(BaseModel):
    expand: StrictStr | None = None
    projects: list[ProjectIssueCreateMetadata] | None = None
