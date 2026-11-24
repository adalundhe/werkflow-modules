from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .project_details import ProjectDetails


class Scope(BaseModel):
    model_config = ConfigDict(extra="allow")

    project: ProjectDetails | None = None
    type: StrictStr | None = None
