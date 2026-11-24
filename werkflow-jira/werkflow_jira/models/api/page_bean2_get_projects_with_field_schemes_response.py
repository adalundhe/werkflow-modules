from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .get_projects_with_field_schemes_response import GetProjectsWithFieldSchemesResponse


class PageBean2GetProjectsWithFieldSchemesResponse(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[GetProjectsWithFieldSchemesResponse] | None = None
