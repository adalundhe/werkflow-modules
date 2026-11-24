from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_user_hierarchy_group_search_criteria import ConnectUserHierarchyGroupSearchCriteria
from .connect_user_hierarchy_group_search_filter import ConnectUserHierarchyGroupSearchFilter


class ConnectSearchUserHierarchyGroupsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectUserHierarchyGroupSearchFilter | None = None
    SearchCriteria: ConnectUserHierarchyGroupSearchCriteria | None = None
