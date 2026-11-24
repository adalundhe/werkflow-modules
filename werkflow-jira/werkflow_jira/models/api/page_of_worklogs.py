from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt
from .worklog import Worklog


class PageOfWorklogs(BaseModel):
    model_config = ConfigDict(extra="allow")

    maxResults: StrictInt | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
    worklogs: list[Worklog] | None = None
