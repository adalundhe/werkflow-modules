from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeStackInstanceRequest(BaseModel):
    StackSetName: StrictStr
    StackInstanceAccount: StrictStr
    StackInstanceRegion: StrictStr
    CallAs: Literal['SELF', 'DELEGATED_ADMIN'] | None = None
