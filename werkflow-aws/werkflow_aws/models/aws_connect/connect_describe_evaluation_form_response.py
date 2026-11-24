from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_evaluation_form import ConnectEvaluationForm


class ConnectDescribeEvaluationFormResponse(BaseModel):
    EvaluationForm: ConnectEvaluationForm | None = None
    ResponseMetadata: dict[str, Any] | None = None
