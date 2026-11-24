from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .project_field_bean import ProjectFieldBean


class PageBean2ProjectFieldBean(BaseModel):
    isLast: StrictBool | None = None
    maxResults: StrictInt | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    values: list[ProjectFieldBean] | None = None
