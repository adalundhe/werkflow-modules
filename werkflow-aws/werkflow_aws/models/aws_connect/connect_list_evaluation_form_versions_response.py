from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_version_summary import ConnectEvaluationFormVersionSummary


class ConnectListEvaluationFormVersionsResponse(BaseModel):
    EvaluationFormVersionSummaryList: list[ConnectEvaluationFormVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
