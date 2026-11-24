from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IssuesAndJQLQueries(BaseModel):
    issueIds: list[StrictInt] | None = None
    jqls: list[StrictStr] | None = None
