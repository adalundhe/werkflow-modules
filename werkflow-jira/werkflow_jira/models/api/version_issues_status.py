from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt


class VersionIssuesStatus(BaseModel):
    model_config = ConfigDict(extra="allow")

    done: StrictInt | None = None
    inProgress: StrictInt | None = None
    toDo: StrictInt | None = None
    unmapped: StrictInt | None = None
