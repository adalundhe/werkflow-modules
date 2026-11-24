from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .project_details import ProjectDetails


class PageBeanProjectDetails(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[ProjectDetails] | None = None
