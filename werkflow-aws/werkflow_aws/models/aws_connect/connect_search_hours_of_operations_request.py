from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_hours_of_operation_search_criteria import ConnectHoursOfOperationSearchCriteria
from .connect_hours_of_operation_search_filter import ConnectHoursOfOperationSearchFilter


class ConnectSearchHoursOfOperationsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectHoursOfOperationSearchFilter | None = None
    SearchCriteria: ConnectHoursOfOperationSearchCriteria | None = None
