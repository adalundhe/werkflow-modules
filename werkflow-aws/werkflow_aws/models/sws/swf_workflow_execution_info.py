from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .swf_workflow_execution import SWFWorkflowExecution
from .swf_workflow_type import SWFWorkflowType


class SWFWorkflowExecutionInfo(BaseModel):
    execution: SWFWorkflowExecution | None = None
    workflowType: SWFWorkflowType | None = None
    startTimestamp: datetime.datetime | StrictStr | None = None
    closeTimestamp: datetime.datetime | StrictStr | None = None
    executionStatus: StrictStr | None = None
    closeStatus: StrictStr | None = None
    parent: SWFWorkflowExecution | None = None
    tagList: list[StrictStr] | None = None
    cancelRequested: StrictBool | None = None
