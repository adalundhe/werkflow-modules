from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_project_usage_page import StatusProjectUsagePage


class StatusProjectUsageDTO(BaseModel):
    projects: StatusProjectUsagePage | None = None
    statusId: StrictStr | None = None
