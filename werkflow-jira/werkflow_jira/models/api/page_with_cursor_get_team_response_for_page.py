from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .get_team_response_for_page import GetTeamResponseForPage


class PageWithCursorGetTeamResponseForPage(BaseModel):
    cursor: StrictStr | None = None
    last: StrictBool | None = None
    nextPageCursor: StrictStr | None = None
    size: StrictInt | None = None
    total: StrictInt | None = None
    values: list[GetTeamResponseForPage] | None = None
