from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexDescribeTestExecutionRequest(BaseModel):
    testExecutionId: StrictStr
