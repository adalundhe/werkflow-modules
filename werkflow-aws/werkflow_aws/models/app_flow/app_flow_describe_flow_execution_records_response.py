from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_flow_execution_record import AppFlowExecutionRecord


class AppFlowDescribeFlowExecutionRecordsResponse(BaseModel):
    flowExecutions: list[AppFlowExecutionRecord] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
