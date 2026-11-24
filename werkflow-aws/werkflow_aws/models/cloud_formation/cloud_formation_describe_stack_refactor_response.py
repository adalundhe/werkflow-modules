from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackRefactorResponse(BaseModel):
    Description: StrictStr | None = None
    StackRefactorId: StrictStr | None = None
    StackIds: list[StrictStr] | None = None
    ExecutionStatus: StrictStr | None = None
    ExecutionStatusReason: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
