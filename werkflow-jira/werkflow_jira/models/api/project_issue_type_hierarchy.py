from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .project_issue_types_hierarchy_level import ProjectIssueTypesHierarchyLevel


class ProjectIssueTypeHierarchy(BaseModel):
    hierarchy: list[ProjectIssueTypesHierarchyLevel] | None = None
    projectId: StrictInt | None = None
