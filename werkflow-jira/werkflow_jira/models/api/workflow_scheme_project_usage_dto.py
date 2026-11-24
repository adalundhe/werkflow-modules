from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_usage_page import ProjectUsagePage


class WorkflowSchemeProjectUsageDTO(BaseModel):
    projects: ProjectUsagePage | None = None
    workflowSchemeId: StrictStr | None = None
