from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_list_events_filters import DevOpsGuruListEventsFilters


class DevOpsGuruListEventsRequest(BaseModel):
    Filters: DevOpsGuruListEventsFilters
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    AccountId: StrictStr | None = None
