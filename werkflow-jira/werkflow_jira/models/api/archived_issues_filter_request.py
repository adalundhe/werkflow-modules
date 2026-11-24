from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .date_range_filter_request import DateRangeFilterRequest


class ArchivedIssuesFilterRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    archivedBy: list[StrictStr] | None = None
    archivedDateRange: DateRangeFilterRequest | None = None
    issueTypes: list[StrictStr] | None = None
    projects: list[StrictStr] | None = None
    reporters: list[StrictStr] | None = None
