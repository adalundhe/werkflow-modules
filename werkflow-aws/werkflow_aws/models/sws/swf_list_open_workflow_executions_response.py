from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .swf_workflow_execution_info import SWFWorkflowExecutionInfo


class SWFListOpenWorkflowExecutionsResponse(BaseModel):
    executionInfos: list[SWFWorkflowExecutionInfo] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
