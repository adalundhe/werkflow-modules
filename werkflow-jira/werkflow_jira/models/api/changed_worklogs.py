from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .changed_worklog import ChangedWorklog


class ChangedWorklogs(BaseModel):
    lastPage: StrictBool | None = None
    nextPage: StrictStr | None = None
    self: StrictStr | None = None
    since: StrictInt | None = None
    until: StrictInt | None = None
    values: list[ChangedWorklog] | None = None
