from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .iam_deletion_task_failure_reason_type import IAMDeletionTaskFailureReasonType


class IAMGetServiceLinkedRoleDeletionStatusResponse(BaseModel):
    Status: StrictStr | None = None
    Reason: IAMDeletionTaskFailureReasonType | None = None
    ResponseMetadata: dict[str, Any] | None = None
