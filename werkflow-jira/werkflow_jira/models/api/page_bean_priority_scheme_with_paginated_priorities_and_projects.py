from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .priority_scheme_with_paginated_priorities_and_projects import PrioritySchemeWithPaginatedPrioritiesAndProjects


class PageBeanPrioritySchemeWithPaginatedPrioritiesAndProjects(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[PrioritySchemeWithPaginatedPrioritiesAndProjects] | None = None
