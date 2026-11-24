from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .project_data_policy import ProjectDataPolicy


class ProjectWithDataPolicy(BaseModel):
    dataPolicy: ProjectDataPolicy | None = None
    id: StrictInt | None = None
