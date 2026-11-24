from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_execution_record import ConnectExecutionRecord


class ConnectListTestCaseExecutionRecordsResponse(BaseModel):
    ExecutionRecords: list[ConnectExecutionRecord] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
