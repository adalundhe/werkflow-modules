from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_execution_time_filter import SWFExecutionTimeFilter
from .swf_tag_filter import SWFTagFilter
from .swf_workflow_execution_filter import SWFWorkflowExecutionFilter
from .swf_workflow_type_filter import SWFWorkflowTypeFilter


class SWFCountOpenWorkflowExecutionsRequest(BaseModel):
    domain: StrictStr
    startTimeFilter: SWFExecutionTimeFilter
    typeFilter: SWFWorkflowTypeFilter | None = None
    tagFilter: SWFTagFilter | None = None
    executionFilter: SWFWorkflowExecutionFilter | None = None
