from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_queue_search_criteria import ConnectQueueSearchCriteria
from .connect_queue_search_filter import ConnectQueueSearchFilter


class ConnectSearchQueuesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectQueueSearchFilter | None = None
    SearchCriteria: ConnectQueueSearchCriteria | None = None
