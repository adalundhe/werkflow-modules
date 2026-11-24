from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectStartTestCaseExecutionRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr
    ClientToken: StrictStr | None = None
