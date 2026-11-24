from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_search_criteria import ConnectEvaluationSearchCriteria
from .connect_evaluation_search_filter import ConnectEvaluationSearchFilter


class ConnectSearchContactEvaluationsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchCriteria: ConnectEvaluationSearchCriteria | None = None
    SearchFilter: ConnectEvaluationSearchFilter | None = None
