from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneProjectsForRule(BaseModel):
    selectionMode: StrictStr | None = None
    specificProjects: list[StrictStr] | None = None
