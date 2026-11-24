from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .swf_task_list import SWFTaskList


class SWFPollForDecisionTaskRequest(BaseModel):
    domain: StrictStr
    taskList: SWFTaskList
    identity: StrictStr | None = None
    nextPageToken: StrictStr | None = None
    maximumPageSize: StrictInt | None = None
    reverseOrder: StrictBool | None = None
    startAtPreviousStartedEvent: StrictBool | None = None
