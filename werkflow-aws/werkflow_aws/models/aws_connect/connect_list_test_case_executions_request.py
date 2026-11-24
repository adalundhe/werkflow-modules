from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListTestCaseExecutionsRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr | None = None
    TestCaseName: StrictStr | None = None
    StartTime: StrictInt | None = None
    EndTime: StrictInt | None = None
    Status: Literal['INITIATED', 'PASSED', 'FAILED', 'IN_PROGRESS', 'STOPPED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
