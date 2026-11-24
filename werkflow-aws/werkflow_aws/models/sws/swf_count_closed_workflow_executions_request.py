from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_close_status_filter import SWFCloseStatusFilter
from .swf_execution_time_filter import SWFExecutionTimeFilter
from .swf_tag_filter import SWFTagFilter
from .swf_workflow_execution_filter import SWFWorkflowExecutionFilter
from .swf_workflow_type_filter import SWFWorkflowTypeFilter


class SWFCountClosedWorkflowExecutionsRequest(BaseModel):
    domain: StrictStr
    startTimeFilter: SWFExecutionTimeFilter | None = None
    closeTimeFilter: SWFExecutionTimeFilter | None = None
    executionFilter: SWFWorkflowExecutionFilter | None = None
    typeFilter: SWFWorkflowTypeFilter | None = None
    tagFilter: SWFTagFilter | None = None
    closeStatusFilter: SWFCloseStatusFilter | None = None
