from __future__ import annotations
from pydantic import BaseModel
from .bulk_operation_error_result import BulkOperationErrorResult
from .created_issue import CreatedIssue


class CreatedIssues(BaseModel):
    errors: list[BulkOperationErrorResult] | None = None
    issues: list[CreatedIssue] | None = None
