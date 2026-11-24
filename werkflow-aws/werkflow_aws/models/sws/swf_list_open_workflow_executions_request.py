from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .swf_execution_time_filter import SWFExecutionTimeFilter
from .swf_tag_filter import SWFTagFilter
from .swf_workflow_execution_filter import SWFWorkflowExecutionFilter
from .swf_workflow_type_filter import SWFWorkflowTypeFilter


class SWFListOpenWorkflowExecutionsRequest(BaseModel):
    domain: StrictStr
    startTimeFilter: SWFExecutionTimeFilter
    typeFilter: SWFWorkflowTypeFilter | None = None
    tagFilter: SWFTagFilter | None = None
    nextPageToken: StrictStr | None = None
    maximumPageSize: StrictInt | None = None
    reverseOrder: StrictBool | None = None
    executionFilter: SWFWorkflowExecutionFilter | None = None
