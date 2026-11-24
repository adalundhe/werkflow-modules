from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class StepFunctionsDescribeStateMachineForExecutionRequest(BaseModel):
    executionArn: StrictStr
    includedData: Literal['ALL_DATA', 'METADATA_ONLY'] | None = None
