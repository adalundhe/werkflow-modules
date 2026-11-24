from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListTestCaseExecutionRecordsRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr
    TestCaseExecutionId: StrictStr
    Status: Literal['INITIATED', 'PASSED', 'FAILED', 'IN_PROGRESS', 'STOPPED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
