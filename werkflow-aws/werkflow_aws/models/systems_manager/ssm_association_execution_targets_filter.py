from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMAssociationExecutionTargetsFilter(BaseModel):
    Key: Literal['Status', 'ResourceId', 'ResourceType']
    Value: StrictStr
