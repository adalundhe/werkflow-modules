from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectDescribeTestCaseRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr
    Status: Literal['PUBLISHED', 'SAVED'] | None = None
