from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .changelog import Changelog


class PageOfChangelogs(BaseModel):
    histories: list[Changelog] | None = None
    maxResults: StrictInt | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
