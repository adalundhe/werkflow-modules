from __future__ import annotations
from pydantic import BaseModel
from .project_issue_type_mapping import ProjectIssueTypeMapping


class ProjectIssueTypeMappings(BaseModel):
    mappings: list[ProjectIssueTypeMapping] | None = None
