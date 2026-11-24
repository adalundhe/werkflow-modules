from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_search_summary import ConnectEvaluationSearchSummary


class ConnectSearchContactEvaluationsResponse(BaseModel):
    EvaluationSearchSummaryList: list[ConnectEvaluationSearchSummary] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
