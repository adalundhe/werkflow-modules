from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectStopTestCaseExecutionRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseExecutionId: StrictStr
    TestCaseId: StrictStr
    ClientToken: StrictStr | None = None
