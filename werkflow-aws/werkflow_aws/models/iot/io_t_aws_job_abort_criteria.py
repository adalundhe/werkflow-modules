from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class IoTAwsJobAbortCriteria(BaseModel):
    failureType: Literal['FAILED', 'REJECTED', 'TIMED_OUT', 'ALL']
    action: Literal['CANCEL']
    thresholdPercentage: StrictFloat | StrictInt
    minNumberOfExecutedThings: StrictInt
