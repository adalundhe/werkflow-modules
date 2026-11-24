from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comment import Comment


class PaginatedResponseComment(BaseModel):
    maxResults: StrictInt | None = None
    results: list[Comment] | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
