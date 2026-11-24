from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .status_project_usage import StatusProjectUsage


class StatusProjectUsagePage(BaseModel):
    nextPageToken: StrictStr | None = None
    values: list[StatusProjectUsage] | None = None
