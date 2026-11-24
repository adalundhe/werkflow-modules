from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .swf_workflow_execution_configuration import SWFWorkflowExecutionConfiguration
from .swf_workflow_execution_info import SWFWorkflowExecutionInfo
from .swf_workflow_execution_open_counts import SWFWorkflowExecutionOpenCounts


class SWFDescribeWorkflowExecutionResponse(BaseModel):
    executionInfo: SWFWorkflowExecutionInfo | None = None
    executionConfiguration: SWFWorkflowExecutionConfiguration | None = None
    openCounts: SWFWorkflowExecutionOpenCounts | None = None
    latestActivityTaskTimestamp: datetime.datetime | StrictStr | None = None
    latestExecutionContext: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
