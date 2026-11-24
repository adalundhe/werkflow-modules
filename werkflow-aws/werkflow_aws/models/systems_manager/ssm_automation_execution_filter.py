from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMAutomationExecutionFilter(BaseModel):
    Key: Literal['DocumentNamePrefix', 'ExecutionStatus', 'ExecutionId', 'ParentExecutionId', 'CurrentAction', 'StartTimeBefore', 'StartTimeAfter', 'AutomationType', 'TagKey', 'TargetResourceGroup', 'AutomationSubtype', 'OpsItemId']
    Values: list[StrictStr]
