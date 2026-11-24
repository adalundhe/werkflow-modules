from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .status_details import StatusDetails


class IssueTypeWithStatus(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
    statuses: list[StatusDetails] | None = None
    subtask: StrictBool | None = None
