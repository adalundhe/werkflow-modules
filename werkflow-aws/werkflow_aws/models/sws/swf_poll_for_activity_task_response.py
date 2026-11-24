from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_activity_type import SWFActivityType
from .swf_workflow_execution import SWFWorkflowExecution


class SWFPollForActivityTaskResponse(BaseModel):
    taskToken: StrictStr | None = None
    activityId: StrictStr | None = None
    startedEventId: StrictInt | None = None
    workflowExecution: SWFWorkflowExecution | None = None
    activityType: SWFActivityType | None = None
    input: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
