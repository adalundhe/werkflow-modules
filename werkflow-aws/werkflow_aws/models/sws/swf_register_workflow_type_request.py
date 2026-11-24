from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .swf_task_list import SWFTaskList


class SWFRegisterWorkflowTypeRequest(BaseModel):
    domain: StrictStr
    name: StrictStr
    version: StrictStr
    description: StrictStr | None = None
    defaultTaskStartToCloseTimeout: StrictStr | None = None
    defaultExecutionStartToCloseTimeout: StrictStr | None = None
    defaultTaskList: SWFTaskList | None = None
    defaultTaskPriority: StrictStr | None = None
    defaultChildPolicy: Literal['TERMINATE', 'REQUEST_CANCEL', 'ABANDON'] | None = None
    defaultLambdaRole: StrictStr | None = None
