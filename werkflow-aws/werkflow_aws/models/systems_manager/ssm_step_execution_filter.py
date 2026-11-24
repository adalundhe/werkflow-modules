from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMStepExecutionFilter(BaseModel):
    Key: Literal['StartTimeBefore', 'StartTimeAfter', 'StepExecutionStatus', 'StepExecutionId', 'StepName', 'Action', 'ParentStepExecutionId', 'ParentStepIteration', 'ParentStepIteratorValue']
    Values: list[StrictStr]
