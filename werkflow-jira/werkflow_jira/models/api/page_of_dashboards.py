from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dashboard import Dashboard


class PageOfDashboards(BaseModel):
    dashboards: list[Dashboard] | None = None
    maxResults: StrictInt | None = None
    next: StrictStr | None = None
    prev: StrictStr | None = None
    startAt: StrictInt | None = None
    total: StrictInt | None = None
