from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class StepFunctionsDescribeStateMachineRequest(BaseModel):
    stateMachineArn: StrictStr
    includedData: Literal['ALL_DATA', 'METADATA_ONLY'] | None = None
