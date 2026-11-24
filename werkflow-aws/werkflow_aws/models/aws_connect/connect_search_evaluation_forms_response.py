from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_form_search_summary import ConnectEvaluationFormSearchSummary


class ConnectSearchEvaluationFormsResponse(BaseModel):
    EvaluationFormSearchSummaryList: list[ConnectEvaluationFormSearchSummary] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
