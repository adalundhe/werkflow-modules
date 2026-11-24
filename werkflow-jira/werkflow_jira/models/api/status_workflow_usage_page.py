from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_workflow_usage_workflow import StatusWorkflowUsageWorkflow


class StatusWorkflowUsagePage(BaseModel):
    nextPageToken: StrictStr | None = None
    values: list[StatusWorkflowUsageWorkflow] | None = None
