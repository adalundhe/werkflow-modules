from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_resource_tags_search_criteria import ConnectResourceTagsSearchCriteria


class ConnectSearchResourceTagsRequest(BaseModel):
    InstanceId: StrictStr
    ResourceTypes: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchCriteria: ConnectResourceTagsSearchCriteria | None = None
