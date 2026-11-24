from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationSignalResourceRequest(BaseModel):
    StackName: StrictStr
    LogicalResourceId: StrictStr
    UniqueId: StrictStr
    Status: Literal['SUCCESS', 'FAILURE']
