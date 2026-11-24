from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IssueCommentListRequestBean(BaseModel):
    ids: list[StrictInt] | None = None
