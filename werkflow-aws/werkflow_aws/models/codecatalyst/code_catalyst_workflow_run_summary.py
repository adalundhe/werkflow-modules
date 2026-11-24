from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_catalyst_workflow_run_status_reason import CodeCatalystWorkflowRunStatusReason


class CodeCatalystWorkflowRunSummary(BaseModel):
    id: StrictStr | None = None
    workflowId: StrictStr | None = None
    workflowName: StrictStr | None = None
    status: StrictStr | None = None
    statusReasons: list[CodeCatalystWorkflowRunStatusReason] | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
