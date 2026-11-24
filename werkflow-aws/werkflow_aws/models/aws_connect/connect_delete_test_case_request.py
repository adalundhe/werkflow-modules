from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteTestCaseRequest(BaseModel):
    InstanceId: StrictStr
    TestCaseId: StrictStr
