from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFormationListStackRefactorsRequest(BaseModel):
    ExecutionStatusFilter: list[Literal['UNAVAILABLE', 'AVAILABLE', 'OBSOLETE', 'EXECUTE_IN_PROGRESS', 'EXECUTE_COMPLETE', 'EXECUTE_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED']] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
