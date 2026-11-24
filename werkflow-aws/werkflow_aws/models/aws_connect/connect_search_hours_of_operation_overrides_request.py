from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_hours_of_operation_override_search_criteria import ConnectHoursOfOperationOverrideSearchCriteria
from .connect_hours_of_operation_search_filter import ConnectHoursOfOperationSearchFilter


class ConnectSearchHoursOfOperationOverridesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectHoursOfOperationSearchFilter | None = None
    SearchCriteria: ConnectHoursOfOperationOverrideSearchCriteria | None = None
