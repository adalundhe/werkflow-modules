from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_id import ProjectId


class WorkflowScope(BaseModel):
    project: ProjectId | None = None
    type: StrictStr | None = None
