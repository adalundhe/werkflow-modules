from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationOperationEntry(BaseModel):
    OperationType: StrictStr | None = None
    OperationId: StrictStr | None = None
