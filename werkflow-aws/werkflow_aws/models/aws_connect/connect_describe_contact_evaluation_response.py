from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_evaluation import ConnectEvaluation
from .connect_evaluation_form_content import ConnectEvaluationFormContent


class ConnectDescribeContactEvaluationResponse(BaseModel):
    Evaluation: ConnectEvaluation | None = None
    EvaluationForm: ConnectEvaluationFormContent | None = None
    ResponseMetadata: dict[str, Any] | None = None
