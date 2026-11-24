from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .swf_history_event import SWFHistoryEvent
from .swf_workflow_execution import SWFWorkflowExecution
from .swf_workflow_type import SWFWorkflowType


class SWFPollForDecisionTaskResponse(BaseModel):
    taskToken: StrictStr | None = None
    startedEventId: StrictInt | None = None
    workflowExecution: SWFWorkflowExecution | None = None
    workflowType: SWFWorkflowType | None = None
    events: list[SWFHistoryEvent] | None = None
    nextPageToken: StrictStr | None = None
    previousStartedEventId: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
