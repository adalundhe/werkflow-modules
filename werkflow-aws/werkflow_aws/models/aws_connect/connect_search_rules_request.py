from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_rules_search_criteria import ConnectRulesSearchCriteria
from .connect_rules_search_filter import ConnectRulesSearchFilter


class ConnectSearchRulesRequest(BaseModel):
    InstanceId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    SearchCriteria: ConnectRulesSearchCriteria | None = None
    SearchFilter: ConnectRulesSearchFilter | None = None
