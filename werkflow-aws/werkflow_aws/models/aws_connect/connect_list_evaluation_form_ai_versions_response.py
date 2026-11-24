from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_ai_version_summary import ConnectEvaluationFormAIVersionSummary


class ConnectListEvaluationFormAIVersionsResponse(BaseModel):
    AIVersionSummaries: list[ConnectEvaluationFormAIVersionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
