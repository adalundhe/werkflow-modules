from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_aggregate_evaluation_result import ConfigServiceAggregateEvaluationResult


class ConfigServiceGetAggregateComplianceDetailsByConfigRuleResponse(BaseModel):
    AggregateEvaluationResults: list[ConfigServiceAggregateEvaluationResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
