from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_predefined_attribute_search_criteria import ConnectPredefinedAttributeSearchCriteria


class ConnectSearchPredefinedAttributesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchCriteria: ConnectPredefinedAttributeSearchCriteria | None = None
