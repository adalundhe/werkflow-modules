from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_usage_page import ProjectUsagePage


class WorkflowProjectUsageDTO(BaseModel):
    projects: ProjectUsagePage | None = None
    workflowId: StrictStr | None = None
