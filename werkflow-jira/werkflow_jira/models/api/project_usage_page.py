from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_usage import ProjectUsage


class ProjectUsagePage(BaseModel):
    nextPageToken: StrictStr | None = None
    values: list[ProjectUsage] | None = None
