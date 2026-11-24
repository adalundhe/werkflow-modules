from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_summary import ConnectEvaluationFormSummary


class ConnectListEvaluationFormsResponse(BaseModel):
    EvaluationFormSummaryList: list[ConnectEvaluationFormSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
