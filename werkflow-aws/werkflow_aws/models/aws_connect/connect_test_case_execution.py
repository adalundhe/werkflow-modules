from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectTestCaseExecution(BaseModel):
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    TestCaseExecutionId: StrictStr | None = None
    TestCaseId: StrictStr | None = None
    TestCaseExecutionStatus: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
