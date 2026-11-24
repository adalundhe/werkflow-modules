from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_security_profile_search_criteria import ConnectSecurityProfileSearchCriteria
from .connect_security_profiles_search_filter import ConnectSecurityProfilesSearchFilter


class ConnectSearchSecurityProfilesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchCriteria: ConnectSecurityProfileSearchCriteria | None = None
    SearchFilter: ConnectSecurityProfilesSearchFilter | None = None
