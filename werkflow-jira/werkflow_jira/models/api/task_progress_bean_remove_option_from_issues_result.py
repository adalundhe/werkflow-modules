from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .remove_option_from_issues_result import RemoveOptionFromIssuesResult


class TaskProgressBeanRemoveOptionFromIssuesResult(BaseModel):
    description: StrictStr | None = None
    elapsedRuntime: StrictInt | None = None
    finished: StrictInt | None = None
    id: StrictStr | None = None
    lastUpdate: StrictInt | None = None
    message: StrictStr | None = None
    progress: StrictInt | None = None
    result: RemoveOptionFromIssuesResult | None = None
    self: StrictStr | None = None
    started: StrictInt | None = None
    status: StrictStr | None = None
    submitted: StrictInt | None = None
    submittedBy: StrictInt | None = None
