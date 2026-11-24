from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFWorkflowTypeConfiguration(BaseModel):
    defaultTaskStartToCloseTimeout: StrictStr | None = None
    defaultExecutionStartToCloseTimeout: StrictStr | None = None
    defaultTaskList: SWFTaskList | None = None
    defaultTaskPriority: StrictStr | None = None
    defaultChildPolicy: StrictStr | None = None
    defaultLambdaRole: StrictStr | None = None
