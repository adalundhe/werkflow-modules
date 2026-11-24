from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_test_case_search_criteria import ConnectTestCaseSearchCriteria
from .connect_test_case_search_filter import ConnectTestCaseSearchFilter


class ConnectSearchTestCasesRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectTestCaseSearchFilter | None = None
    SearchCriteria: ConnectTestCaseSearchCriteria | None = None
