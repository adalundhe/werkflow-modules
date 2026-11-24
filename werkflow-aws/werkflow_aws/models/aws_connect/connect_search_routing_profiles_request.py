from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_routing_profile_search_criteria import ConnectRoutingProfileSearchCriteria
from .connect_routing_profile_search_filter import ConnectRoutingProfileSearchFilter


class ConnectSearchRoutingProfilesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectRoutingProfileSearchFilter | None = None
    SearchCriteria: ConnectRoutingProfileSearchCriteria | None = None
