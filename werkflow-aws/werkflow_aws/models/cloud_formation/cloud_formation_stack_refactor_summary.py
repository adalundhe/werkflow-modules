from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationStackRefactorSummary(BaseModel):
    StackRefactorId: StrictStr | None = None
    Description: StrictStr | None = None
    ExecutionStatus: StrictStr | None = None
    ExecutionStatusReason: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
