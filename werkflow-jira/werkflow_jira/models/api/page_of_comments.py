from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt
from .comment import Comment


class PageOfComments(BaseModel):
    model_config = ConfigDict(extra="allow")

    comments: list[Comment] | None = None
    maxResults: StrictInt | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
