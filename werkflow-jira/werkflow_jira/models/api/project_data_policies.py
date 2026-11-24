from __future__ import annotations
from pydantic import BaseModel
from .project_with_data_policy import ProjectWithDataPolicy


class ProjectDataPolicies(BaseModel):
    projectDataPolicies: list[ProjectWithDataPolicy] | None = None
