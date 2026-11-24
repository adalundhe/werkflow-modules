from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_workflow_usage_page import StatusWorkflowUsagePage


class StatusWorkflowUsageDTO(BaseModel):
    statusId: StrictStr | None = None
    workflows: StatusWorkflowUsagePage | None = None
