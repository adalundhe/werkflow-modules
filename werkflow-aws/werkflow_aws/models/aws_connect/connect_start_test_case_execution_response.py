from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectStartTestCaseExecutionResponse(BaseModel):
    TestCaseExecutionId: StrictStr | None = None
    TestCaseId: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
