from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .user import User


class BulkOperationProgress(BaseModel):
    created: StrictStr | None = None
    failedAccessibleIssues: dict[StrictStr, list[StrictStr]] | None = None
    invalidOrInaccessibleIssueCount: StrictInt | None = None
    processedAccessibleIssues: list[StrictInt] | None = None
    progressPercent: StrictInt | None = None
    started: StrictStr | None = None
    status: StrictStr | None = None
    submittedBy: User | None = None
    taskId: StrictStr | None = None
    totalIssueCount: StrictInt | None = None
    updated: StrictStr | None = None
