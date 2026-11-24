from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_evaluation_result import ConfigServiceEvaluationResult


class ConfigServiceGetComplianceDetailsByConfigRuleResponse(BaseModel):
    EvaluationResults: list[ConfigServiceEvaluationResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
