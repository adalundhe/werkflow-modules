from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .get_plan_response_for_page import GetPlanResponseForPage


class PageWithCursorGetPlanResponseForPage(BaseModel):
    cursor: StrictStr | None = None
    last: StrictBool | None = None
    nextPageCursor: StrictStr | None = None
    size: StrictInt | None = None
    total: StrictInt | None = None
    values: list[GetPlanResponseForPage] | None = None
