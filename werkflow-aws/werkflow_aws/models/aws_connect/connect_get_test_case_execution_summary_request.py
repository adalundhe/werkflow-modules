from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetTestCaseExecutionSummaryRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr
    TestCaseExecutionId: StrictStr
