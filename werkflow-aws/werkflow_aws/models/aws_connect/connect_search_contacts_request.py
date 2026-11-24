from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_search_contacts_time_range import ConnectSearchContactsTimeRange
from .connect_search_criteria import ConnectSearchCriteria
from .connect_sort import ConnectSort


class ConnectSearchContactsRequest(BaseModel):
    InstanceId: StrictStr
    TimeRange: ConnectSearchContactsTimeRange
    SearchCriteria: ConnectSearchCriteria | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Sort: ConnectSort | None = None
