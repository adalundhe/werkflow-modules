from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_scheme_usage_page import WorkflowSchemeUsagePage


class WorkflowSchemeUsageDTO(BaseModel):
    workflowId: StrictStr | None = None
    workflowSchemes: WorkflowSchemeUsagePage | None = None
