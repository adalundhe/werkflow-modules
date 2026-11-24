from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_config_rule_evaluation_status import ConfigServiceConfigRuleEvaluationStatus


class ConfigServiceDescribeConfigRuleEvaluationStatusResponse(BaseModel):
    ConfigRulesEvaluationStatus: list[ConfigServiceConfigRuleEvaluationStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
