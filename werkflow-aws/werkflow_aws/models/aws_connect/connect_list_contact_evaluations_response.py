from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_evaluation_summary import ConnectEvaluationSummary


class ConnectListContactEvaluationsResponse(BaseModel):
    EvaluationSummaryList: list[ConnectEvaluationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
