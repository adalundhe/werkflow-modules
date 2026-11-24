from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_form_search_criteria import ConnectEvaluationFormSearchCriteria
from .connect_evaluation_form_search_filter import ConnectEvaluationFormSearchFilter


class ConnectSearchEvaluationFormsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchCriteria: ConnectEvaluationFormSearchCriteria | None = None
    SearchFilter: ConnectEvaluationFormSearchFilter | None = None
