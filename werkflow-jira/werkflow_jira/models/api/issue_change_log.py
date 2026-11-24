from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .changelog import Changelog


class IssueChangeLog(BaseModel):
    changeHistories: list[Changelog] | None = None
    issueId: StrictStr | None = None
