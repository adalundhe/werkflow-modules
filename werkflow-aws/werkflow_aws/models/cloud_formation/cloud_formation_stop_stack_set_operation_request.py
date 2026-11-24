from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationStopStackSetOperationRequest(BaseModel):
    StackSetName: StrictStr
    OperationId: StrictStr
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
