from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_test_case_execution import ConnectTestCaseExecution


class ConnectListTestCaseExecutionsResponse(BaseModel):
    TestCaseExecutions: list[ConnectTestCaseExecution] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
