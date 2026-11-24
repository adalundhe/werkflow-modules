from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMAssociationExecutionFilter(BaseModel):
    Key: Literal['ExecutionId', 'Status', 'CreatedTime']
    Value: StrictStr
    Type: Literal['EQUAL', 'LESS_THAN', 'GREATER_THAN']
